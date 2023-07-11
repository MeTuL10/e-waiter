import mysql.connector as msql

mydb=msql.connect(host='localhost',user='root',passwd='user123')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE restaurant')
mycursor.execute('use restaurant')

mycursor.execute('create table main (m1 int primary key, mname char(50))')
mycursor.execute("insert into main values (1,'INDIAN_APPETIZERS'),(2,'ITALIAN_APPETIZERS'),(3,'INDIAN_MAIN_COURSE'),"+
                 "(4,'INDIAN_BREADS_AND_RICE'),(5,'PIZZAS'),(6,'SANDWICHES'),(7,'SALADS'),(8,'INDIAN_DESSERTS'),(9,'ITALIAN_DESSERTS')")
mycursor.execute('create table INDIAN_APPETIZERS (no int primary key, name char(50),price int)')
mycursor.execute("insert into INDIAN_APPETIZERS values(1,'Assorted Non-veg Platter',399),(2,'Chicken Chaat',350),"+
                 "(3,'Shrimp Pakore',250),(4,'Shammi Kebab',450),(5,'Chicken Pakore',399),(6,'Hera Bhera Kebab',199),"+
                 "(7,'Onion Bhaji',299),(8,'Vegetable Tikka',199),(9,'Samose',100)")
mycursor.execute("create table ITALIAN_APPETIZERS (no int , name char(50),price int)")
mycursor.execute("insert into ITALIAN_APPETIZERS values (1,'Seasonal soup ',199),(2,'Grilled Artichoke ',350),"+
                 "(3,'Prosciutto Bruschetta ',250),(4,'Italian meatballs ',450),(5,'Chefs board',399),(6,'Grilled cauliflower',199),"+
                 "(7,'Crispy calamari ',299),(8,'White truffle garlic bread ',199),(9,'Zucca chips',100),(10,'Burrata ',200),(11,'Arancini ',200)")
mycursor.execute("create table INDIAN_MAIN_COURSE(no int primary key , name char(50),price int)")
mycursor.execute("insert into INDIAN_MAIN_COURSE values ( 1,'Palace Handi',129),(2,'Murg Chakori',189),(3,'Mango Chicken',200),"+
                 "(4,'Murg Tikka Lajawab',200),(5,'Bombay Shrimp Curry',199),(6,'Achari Kadhai',199),(7,'Vindaloo',299),(8,'Madras Curry',199)")
mycursor.execute("create table INDIAN_BREADS_AND_RICE(no int primary key , name char(50),price int)")
mycursor.execute("insert into INDIAN_BREADS_AND_RICE values (1,'Vegetable Biryani',399),(2,'Shrimp Biryani',399),"+
                 "(3,'Hydrabadi Beef Biryani',300),(4,'Gosht Lamb Biryani',399),(5,'Shahi Chicken Biryani',399),"+
                 "(6,'Bread Basket',299),(7,'TanDoori Roti',199)")
mycursor.execute("create table PIZZAS(no int primary key , name char(50),price int)")
mycursor.execute("insert into PIZZAS values (1,'daily pizza',299),(2,'chefs choice',299),(3,'margherita',199),(4,'prosciutto',199),"+
                 "(5,'funghi',199),(6,'bacon & egg',299),(7,'the pig',199)")
mycursor.execute("create table SANDWICHES(no int primary key , name char(50),price int)")
mycursor.execute("insert into SANDWICHES values (1,'grilled chicken',399),(2,'italian grinder',299),(3,'our famous meatball sandwich',299),"+
                 "(4,'the burger',199)")
mycursor.execute("create table SALADS(no int primary key , name char(50),price int)")
mycursor.execute("insert into SALADS values (1,'Caeser',299),(2,'Arugula & Roasted fennel',199),(3,'Tuscan kale',189),"+
                 "(4,'Seasonal Vegetable',150),(5,'chopped Chicken',300),(6,'Italian Farm',200)")
mycursor.execute("create table INDIAN_DESSERTS(no int primary key , name char(50),price int)")
mycursor.execute("insert into INDIAN_DESSERTS values (1,'Palace Mango Sundae',199),(2,'Mango Triffle',159),(3,'Mango Kulfi',89),"+
                 "(4,'Pista Kulfi',60),(5,'Gajar Halwa',100),(6,'Gulab Jamun',100),(7,'Shahi Rasmalai',100),(8,'Badamee Kheer',150)")
mycursor.execute("create table ITALIAN_DESSERTS(no int primary key , name char(50),price int)")
mycursor.execute("insert into ITALIAN_DESSERTS values (1,'Biscotti',299),(2,'Pannacota',299),(3,'Gelato',89),(4,'Choco pie',50),"+
                 "(5,'Apple Pie',400),(6,'Tiramissu',90)")
mycursor.execute("create table dish(no int primary key auto_increment , name char(50),price int)")
mycursor.execute("create table ratings(no int primary key auto_increment , clean int,service int,food int)")