## 主題研究與實作 - Week 8
### 主題一：使用 Grid 完成排版
1. 了解 Grid 的基本操作。
2. 利用 Grid 來完成第一週作業的前端排版。


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
><br> [參考資料2](https://medium.com/@michael80402/mysql%E7%B4%A2%E5%BC%95-e002f707a5f4)
2. 請在 member 資料表中加入適當的索引，加快以下 SQL 語句的查詢效率 SELECT * FROM member WHERE username=’test’ and password=’test’
3. 如何驗證查詢效率是否真的變更好了？
