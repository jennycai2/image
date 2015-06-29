compute_retention = function(yr, mo)
{
  # get the previous month
  if (mo == 1)
  {
    pre_mo =12
    pre_yr = yr - 1
  } else {
    pre_mo = mo - 1
    pre_yr = yr
  }

  #eventtype = 'shareriff'
  eventtype = 'keyboardlaunch'
  # unique active users for previous month
  pre_users = ios_combined %>% filter(as.numeric(format(timestamp.y, "%Y")) == pre_yr) %>% filter(as.numeric(format(timestamp.y, "%m")) == pre_mo) %>% filter(eventname==eventtype) %>% group_by(keyboardid) %>% summarize(n=n()) %>% select(keyboardid)

  # unique active user for current month
  cur_users = ios_combined %>% filter(as.numeric(format(timestamp.y, "%Y")) == yr) %>% filter(as.numeric(format(timestamp.y, "%m")) == mo) %>% filter(eventname==eventtype) %>% group_by(keyboardid) %>% summarize(n=n()) %>% select(keyboardid)

  # active in both months
  same_users = pre_users %>% inner_join(cur_users, by='keyboardid') %>% summarize(n=n())

  pre_users = pre_users %>% summarize(n=n())
  retention_rate = 0
  if (pre_users!=0){
      retention_rate = same_users / pre_users
  }
  return(retention_rate)
}

ratios = c()

for(i in 1:8)
{
  ratios[i] = i

}

ratios[1] = compute_retention(yr = 2014, mo = 11)
ratios[2] = compute_retention(yr = 2014, mo = 12)
ratios[3] = compute_retention(yr = 2015, mo = 1)
ratios[4] = compute_retention(yr = 2015, mo = 2)
ratios[5] = compute_retention(yr = 2015, mo = 3)
ratios[6] = compute_retention(yr = 2015, mo = 4)
ratios[7] = compute_retention(yr = 2015, mo = 5)
ratios[8] = compute_retention(yr = 2015, mo = 6)

h = seq(from=1, to=8)
#names(ratios) <- c('id', 'year', 'group')

#ratios %>% mutate(s = 1) %>% ggvis(x = ~s, y = ~ratios) %>% layer_points()
