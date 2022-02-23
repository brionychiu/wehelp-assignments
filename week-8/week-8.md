## 主題研究與實作 - Week 8
### 主題一：使用 Grid 完成排版
1. 了解 Grid 的基本操作。
> CSS屬性的一種
2. 利用 Grid 來完成第一週作業的前端排版。
* 半成品(未做RWD切版，下面灰色部分沒有做得很完美，每個div都套用class，太費工夫)
* display:inline-grid 跟 display:grid 差異[display:grid](https://www.w3schools.com/css/css_grid.asp)
* grid-column: 1/span2 跟 grid-column: 1/2[span](https://www.w3schools.com/cssref/pr_grid-column.asp)
* grid-template-areas:用點可以空一格-->實作無效
* ![image](https://user-images.githubusercontent.com/94620926/155343885-8c1dcbda-869e-4e26-96c8-6a049f761e53.png)
[A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

### 主題三：AJAX 與 CORS
1. 什麼是 CORS？
>  Cross-origin Resource Sharing 跨來源資料共用，如果要在不同origin間傳遞資料的話,要怎麼做,大家可以遵循的共同規範。
2. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到https://www.google.com/ 並取得回應嗎？
> 不能，這是跨來源呼叫API(不會成功)。
3.  我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎？和上述的狀況，差別在哪裡？
> 可以，這跟CORS沒有關係，因為這只是把一個網頁打開而已(用瀏覽器瀏覽網頁)，不是用AJAX拿資料
4.  如何開放我們自己開發的 API，讓別的網站透過 fecth() 或是 XMLHttpRequest 連結，達到如同第 3 點的可能性
>後端API加上了 header：Access-Control-Allow-Origin: *，代表來自任何 origin 的網站都可以用 AJAX 存取這個資源。
<br> [參考資料1](https://blog.huli.tw/2021/02/19/cors-guide-1/)

### 主題四：使用主鍵、索引優化資料庫查詢效率
1. 了解主鍵 (Primary Key) 和索引 (Index) 的觀念。
>primary key 是 index的一種，屬於唯一值(不可重複)，不可為null，一張表格只有一個(兩個pri綁再一起等，但是一起新增，一起刪除)
><br>index 建立索引是能夠將特定值or欄位找出，提高效率找到資料。包含primary key、unique index(不可重複，可null)、non-unique index(可重複，可null)、full-text search(char、varchar、text型態，可null)。
<br> [參考資料2](https://medium.com/@michael80402/mysql%E7%B4%A2%E5%BC%95-e002f707a5f4)
2. 請在 member 資料表中加入適當的索引，加快以下 SQL 語句的查詢效率 SELECT * FROM member WHERE username=’test’ and password=’test’\
>```ALTER TABLE `member` ADD INDEX `signin`(`username`,`password`);``` 
><br>加入名叫signin的combo index
3. 如何驗證查詢效率是否真的變更好了？
>使用EXPLAIN指令，分析一個查詢敘述。
<br>未使用索引，全表搜尋(type:all)，必須檢查行數:4
![未使用索引](https://user-images.githubusercontent.com/94620926/155064354-cddd9038-5d2f-4f39-a23a-9ab3fb1227ad.png)
<br>使用signin索引，索引搜尋(type:ref)，必須檢查行數:1
![使用索引](https://user-images.githubusercontent.com/94620926/155064416-10cc26bd-069d-489e-bc0f-085f8f9e0ee3.png)
![type表](https://user-images.githubusercontent.com/94620926/155064836-51882065-d2db-4402-b0cf-383bb4044e56.png)

<br>[參考資料3](http://n.sfs.tw/content/index/10376)

### 主題五：使用 Connection Pool 連結資料庫
1. 什麼是 Connection Pool？
>連接池，與資料庫連線的快取，介於後端應用程式及資料庫中間，集中管理與資料庫連線。
2. 如何使用官方提供的 mysql-connector-python 套件，建立 Connection Pool。
```dbconfig = {
  "database": "test",
  "user":     "joe"
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      **dbconfig)
```
```
cnx1 = cnxpool.get_connection()
cnx2 = cnxpool.get_connection()
```
[參考資料4](https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html)

3. 需要從資料庫取得查詢資料時，如何從 Connection Pool 取得 Connection，並且在資料操作結束後，返還 Connection 到 Connetion Pool 中。你會如何撰寫程式碼完成上述的標準操作？
```
cursor = cnx1.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
```
```
finally:
    # closing database connection.
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
```
[參考資料5](https://pynative.com/python-database-connection-pooling-with-mysql/)
