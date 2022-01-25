## wehelp-assignment week-5
### 要求三：SQL CRUD
####  1.使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
```markdown
INSERT INTO `member`(`name`,`username`,`password`) VALUES ('謙謙','test','test');
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_1.JPG "pic_1")

![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_2.JPG "pic_2")

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('魚魚','fish','fish_1',88);
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_3.JPG "pic_3")

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('肥肥','cute','cute_1',24);
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_4.JPG "pic_4")

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('安安','pork','pork_1',283);
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_5.JPG "pic_5")

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('熊熊','bear','bear_1',456);
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_6.JPG "pic_6")

####  2.使用 SELECT 指令取得所有在 member 資料表中的會員資料。
```markdown
SELECT * FROM `member`;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_7.JPG "pic_7")

####  3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```markdown
SELECT * FROM `member` ORDER BY `time`DESC;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_8.JPG "pic_8")

####  4.使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```markdown
SELECT * FROM `member`ORDER BY `time` LIMIT 1,3;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_9.JPG "pic_9")

####  5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```markdown
SELECT * FROM `member` WHERE `username`='test';
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_10.JPG "pic_10")

####  6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```markdown
SELECT * FROM `member` WHERE `username`='test' AND `password`='test';
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_11.JPG "pic_11")

####  7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```markdown
UPDATE `member` SET `name`='test_2' WHERE `username`='test';
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_12.JPG "pic_12")

![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_13.JPG "pic_13")

### 要求四：SQL Aggregate Functions
####  1.取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```markdown
SELECT COUNT(*) FROM `member`;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_14.JPG "pic_14")

####  2.取得 member 資料表中，所有會員 follower_count 欄位的總和。
```markdown
SELECT SUM(`follower_count`) FROM `member`;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_15.JPG "pic_15")

####  3.取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```markdown
SELECT AVG(`follower_count`) FROM `member`;
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_16.JPG "pic_16")

### 要求五：SQL JOIN (Optional)
####  1.使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
```markdown
 SELECT `member_id`,`name`,`content` FROM `message` JOIN `member` ON `message`.`member_id`=`member`.`id`;
 ```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_23.JPG "pic_23")

####  2.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
```markdown
SELECT `member_id`,`name`,`username`,`content` FROM `message` JOIN `member` ON `message`.`member_id`=`member`.`id` WHERE `username`='test';
```
![image](https://github.com/brionychiu/wehelp-assignments/blob/main/week-5/pic/pic_24.JPG "pic_24")





