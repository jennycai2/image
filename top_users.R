library(dplyr)

ONE_PERC_TABLE = ORDER_TABLE %>%
filter(!is_na(trans_amount) %>% group_by(date) %>%
summarize(one_perc_amount = sum(trans_amount) / 100.0))

USERS_TO_BE_REWARDED = ORDER_TABLE %>%
left_join(USER_TABLE, by = "order_id") %>%
group_by(date, user_id) %>%
summarize (day_user_amount = sum(trans_amount)) %>%
left_join(ONE_PERC_TABLE, by = "date") %>%
filter(day_user_amount > one_perc_amount) %>%
select(date, user_id)
