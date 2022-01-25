## wehelp-assignment week-5
### 要求三：SQL CRUD
####  1.使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
```markdown
INSERT INTO `member`(`name`,`username`,`password`) VALUES ('謙謙','test','test');
```
![GITHUB](https://github.com/brionychiu/wehelp-assignments/week-5/pic/pic_1.JPG "pic_1")

![GITHUB](https://github.com/brionychiu/wehelp-assignments/week-5/pic/pic_1.JPG "pic_2")

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('魚魚','fish','fish_1',88);
```
>>pic_3

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('肥肥','cute','cute_1',24);
```
>>pic_4

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('安安','pork','pork_1',283);
```
>>pic_5

```markdown
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`)VALUES('熊熊','bear','bear_1',456);
```
>>pic_6

####  2.使用 SELECT 指令取得所有在 member 資料表中的會員資料。
```markdown
SELECT * FROM `member`;
```
>>pic_7

####  3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```markdown
SELECT * FROM `member`ORDER BY `time`;
```
>>pic_8

####  4.使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```markdown
SELECT * FROM `member`ORDER BY `time` LIMIT 1,3;
```
>>pic_9

####  5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```markdown
SELECT * FROM `member` WHERE `username`='test';
```
>>pic_10

####  6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```markdown
SELECT * FROM `member` WHERE `username`='test' AND `password`='test';
```
>>pic_11

####  7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```markdown
UPDATE `member` SET `name`='test_2' WHERE `username`='test';
```
>>pic_12
>>pic_13

### 要求四：SQL Aggregate Functions
####  1.取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```markdown
SELECT COUNT(*) FROM `member`;
```
>>pic_14
####  2.取得 member 資料表中，所有會員 follower_count 欄位的總和。
```markdown
SELECT SUM(`follower_count`) FROM `member`;
```
>>pic_15
####  3.取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```markdown
SELECT AVG(`follower_count`) FROM `member`;
```
>>pic_16

### 要求五：SQL JOIN (Optional)
####  1.在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：(表)
```markdown
CREATE TABLE `message` (`id` BIGINT PRIMARY KEY AUTO_INCREMENT);
```
>>pic_17

```markdown
ALTER TABLE `message` ADD `member_id` BIGINT NOT NULL;
```
>>pic_18

```markdown
ALTER TABLE `message` ADD FOREIGN KEY(`member_id`) REFERENCES `member`(`id`) ON DELETE CASCADE;
```
>>pic_19

```markdown
ALTER TABLE `message` ADD `content` VARCHAR(225) NOT NULL;
```
>>pic_20

```markdown
ALTER TABLE `message` ADD `time` DATETIME NOT NULL DEFAULT NOW();
```
>>pic_21

```markdown
DESCRIBE `message`;
```
>>pic_22

####  2.使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
```markdown
 SELECT `member_id`,`name`,`content` FROM `message` JOIN `member` ON `message`.`member_id`=`member`.`id`;
 ```
>>pic_23

####  3.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
```markdown
SELECT `member_id`,`name`,`username`,`content` FROM `message` JOIN `member` ON `message`.`member_id`=`member`.`id` WHERE `username`='test';
```
>>pic_24





