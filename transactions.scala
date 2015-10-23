

// Spark in Scala

cd /Users/jenny/Downloads/spark-1.5.1-bin-hadoop2.4

bin/spark-shell --master local[*]

The selection of the top 1000 users should include the following steps:
. Parsing of the files
. We wish to contact users using phone numbers that are not in the do not call list.
As this is a phone campaign, there should be at least one phone number per user in the output.
. Selecting the top users based on highest transaction amount for year 2015
. Save the campaign in a file using the following structure:
Customer ID, Customer name, phone list that can be used to contact the user, total transaction amount

Step 1: transform the RDD
keep entries in 2015
do an inner join with users, so we get phone numbers
filter out the entries which is donot call
order the entries, keep 4 columns

val base = "../RadiusDataEngineeringExercise/"
val transRDD = sc.textFile(base + "transactions.txt")

//val transRDD = sc.textFile("/Users/jenny/Downloads/RadiusDataEngineeringExercise/transactions.txt")
val donotcallRDD = sc.textFile("/Users/jenny/Downloads/RadiusDataEngineeringExercise/donotcall.txt").map(x => (x, 1))
val usersRDD = sc.textFile("/Users/jenny/Downloads/RadiusDataEngineeringExercise/users.txt")

//val topU = sc.textFile("/Users/jenny/Downloads/top_users.txt")


//case class Transaction(customerID: Int, amount: Double, year: Int)
//case class Users(customerID: Int, name: String, phone: String)

def isEmail(item: String): Boolean = {
  item.contains("@")
}

def hasPhoneNum(item: String): Boolean = {
  item.contains("-") && item.contains("(")
}

/*
def safe[S, T](f: S => T): S => Either[T, Exception] = {
  new Function[S, Either[T, Exception]] with Serializable {
    def apply(s: S): Either[T, Exception] = {
      try {
        Left(f(s))
      } catch {
        case e: Exception => Right(e)
      }
    }
  }
}
val safeParse = safe(parse)
*/
def parse(items: Array[String]) = {
  val customerID = items(0).toInt
  val customerName = items(1)
  val phoneNum = items(2)//.split(",")
  ((customerID, customerName), phoneNum)
}

case class infoAmount(id:Int, name: String, phone: String, amount:Double)

import java.io._

val transRDD1 = (transRDD
       .map(_.replace("$", ""))
       .map(_.replace("-", ";"))
       .map(_.split(";"))
       //.map{arr => Transaction(arr(0).toInt, arr(1).toDouble, arr(2).toInt)}
       .map{arr => (arr(0).toInt, (arr(1).toDouble, arr(2).toInt))}
       .filter{ case(k, v) => v._2 == 2015}
       .map{ case(k, v) => (k, v._1)}
       .reduceByKey(_ + _)  //merge multiple purchases from the same customer
       //.map{ case(k, v) => idAmount(k, v)}
       //.takeOrdered(1000)(Ordering[Double].reverse.on(x=>x.amount))
       //.top(1000)(Ordering[Double].reverse.on(x=>x.amount))
       //.filter(x => x.year == 2015)
       //.cache()
       )

val topUsersRDD = (usersRDD
       .filter(hasPhoneNum(_)) //if there is no phone number, remove the entry
       .map(_.split(";"))
       .map(_.filter(!isEmail(_)))
       .map(parse)
       .flatMapValues(x => x.split(",")) //if a customer has multiple numbers, generate separate entries
       .map{case (key, value) => (value, key)}
       .subtractByKey(donotcallRDD)
       .filter{case (key, value) => (key != "")}
       .map{case (key, value) => (value, key)}
       .reduceByKey(_ + "," + _)  //merge phone numbers from the same customer
       .map{case (key, phone) => (key._1, (key._2, phone))}
       .join(transRDD1)
       .map{case (id, (info, amount)) => infoAmount(id, info._1, info._2, amount)}
       //.takeOrdered(1000)(Ordering[Double].reverse.on(x=>x.amount))
       )
val topUsers = (topUsersRDD
         .takeOrdered(1000)(Ordering[Double].reverse.on(x=>x.amount))
         .map(x => x.id.toString + ";" + x.name + ";" + x.phone + ";" + "$" + "%.2f".format(x.amount))
       //.map{case (id, ((name, phone), amount)) => (id, name, phone, amount)}
       )

val pw = new PrintWriter(new File("/Users/jenny/Downloads/top_users.txt" ))
for (elem <- topUsers) {
    pw.write(elem)
    pw.write("\n")
}
pw.close

  //Map(4 -> 5, 2 -> 8322, 3 -> 16667, 5 -> 6)
  //Map(4 -> 11, 2 -> 24989)
//case class idAmount(id:Int, amount:Double)
//val transRDD1 = sc.parallelize(trans).map{ x => (x.id, x.amount)}
 //= Map(2015 -> 250091, 2014 -> 249909)
