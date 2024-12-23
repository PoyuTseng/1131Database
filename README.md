# 113-1師大科技系資料庫系統(Database)
# 授課教師
蔡芸琤老師  
[老師的 GitHub](https://github.com/peculab/Database)

## 基本資料
- **姓名**：曾伯宇(Tseng,Po-Yu)
- **系級**：科技系碩士班三年級
- **學號**：61171036H

## 課程筆記區

## 作業連結區
- **H.W1**: [Video](https://www.youtube.com/watch?v=Q4qnY9xTYms)
- **HW01階段性完成日誌**

- 初步設定與結構階段

建立一個簡單的 HTML 結構，用於顯示並新增資料至example_table。
定義基本的 HTML 架構。
設置一個表單（「新增資料表單」），使用 POST 動作提交新資料。
新增一個表格結構來顯示資料，包含 ID、Post 和 Date 等標題。
 
- 端整合資料處理階段

啟用後端來處理表單提交與資料檢索。
處理 POST 請求的路由，以新增資料至資料庫。
配置後端從 example_table 中提取資料供前端顯示。
挑戰： 需要確保前端的資料即時更新。
後續步驟： 完成表單提交處理並實現動態資料渲染。

- 資料綁定與動態顯示階段

動態綁定資料至 HTML 範本，以在表格中顯示每一筆資料。
將 Jinja 模板語法（{% for data in tables %}）與後端資料進行整合。
測試確保每次新提交的資料可即時顯示。

- 樣式設計與優化階段

增強頁面外觀並優化加載性能。
使用 CSS 改善佈局和易讀性。
優化頁面以適應行動設備的顯示。 

過程中出現環境錯誤等狀況，最後透過影片拍攝鍵入資料過程。
- **H.W2**: [Video](https://youtu.be/q18jwjdXXJ8) | [MYSQL Workbench](https://youtu.be/e3B8tasgMGc) | [New ER-diagram](https://github.com/PoyuTseng/1131Database/blob/main/Database-HW02/ER-Diagram.jpg)
- **HW03階段性完成日誌**
- 環境設置：

使用 requirements.txt 限制環境，鎖定以下版本以避免相容性問題：
Flask==3.0.3
mysql-connector==2.2.9
mysql-connector-python==9.0.0
使用 DBeaver 作為 MySQL 的輔助工具，方便資料庫管理和即時查詢。

- 資料庫與表格結構建立：

因範例資料庫中的檔案有互相依存關係，不能單獨使用 故捨棄複製整個範例，改以將範例作為基礎，創立新的表格資料庫。
從範例資料庫中複製 address 表格的框架至新專案的 MySQL 資料庫，作為本作業新form的基礎。
設定 address01-07 七個不同的欄位以收集所需資料項目，並配置 address 表格來對應這些項目。

- 前端表單與基本功能：

透過表單呈現填寫框架，並讓填寫內容能顯示在網頁表格上，形成簡易的 CRUD 架構。
在 ChatGPT 的協助下撰寫 CSS 來美化表格，為按鈕和主要區塊添加直觀的顏色區分，讓介面更符合主題並提升使用者體驗。

- CRUD 功能拓展與顏色區分按鈕：

設置刪除（Delete）和更新（Update）按鈕，並以不同顏色區分正負向操作按鈕（如紅色刪除、綠色更新）。
完成資料更新與刪除的即時顯示功能，確保資料庫變更即時反映在網頁介面上。

- 搜尋功能設置與測試：

加入以 city_ID(城市郵遞區號) 查詢的功能，並將查詢結果顯示在頁面底部。
在 MySQL 與 DBeaver 中即時檢視資料輸入與更新，驗證資料準確性與即時性，確認所有操作功能正常運作。

- **H.W3**: [Video](https://youtu.be/IkiyzLHPZ08)
- **HW03階段性完成日誌**
- MongoDB安裝相關資料建立
  
安裝MongoDB程式並創建new connection串聯

- VScode中環境建構、相關資料建立與執行
  
透過指令:
mkdir noSQL
cd .\noSQL\
python -m venv .vene
於VScode中建立noSQL資料 並 設定環境
pip install Flask pymongo

- noSQL搜尋功能設置與測試執行

透過VScode中noSQL目錄下noSQL.py執行，進入Startup Log頁面中可以看到相關的Document ID與Shwo details等資料
點擊Creat New Entrys切換至Create a New Entry輸入資料頁面
鍵入任意資料Ex Name:Alice / Description:SAO後 點擊Create
畫面跳轉至Startup Log並出現新資料點擊Show details便可查閱剛鍵入之資料
轉換至MongoDB中localhost2707目錄下local中startup_log內點擊Refresh即可看到新鍵入之資料


- **H.W4**: [Video](https://youtu.be/CQaoB5r4HIk?si=ZhCgXX9F0RGE96Hg)
- **HW04階段性完成日誌**
- MongoDB相關問題排除
  
在透過MongoDB程式串聯VScode環境建構時遇到
ModuleNotFoundError: No module named 'bson'
ImportError: cannot import name 'SON' from 'bson' (d:\1131DB\1131Database\.vene\Lib\site-packages\bson\__init__.py)
ModuleNotFoundError: No module named 'bson.objectid'
等相關問題。
透過安裝 pymongo 與 確保只使用 pymongo 的 bson 等方式進行排除
卸載可能導致衝突的獨立 bson 套件：
pip uninstall bson
pip uninstall pymongo
重新安裝 正確版本的 pymongo（這會自動包含適當的 bson 模組）：
pip install pymongo
這樣可以確保 bson 是由 pymongo 提供的，且包含 SON。

- 透過noSQL功能設置與測試執行

透過VScode中noSQL目錄下noSQL.py執行，進入Startup Log頁面中可以看到相關的Document ID與Shwo details等資料
點擊Creat New Entrys切換至Create a New Entry輸入資料頁面
鍵入任意資料後 點擊Create
透過Show/Hide顯示或隱藏資料列
並且可以對資料進行刪除與編輯修改
畫面跳轉至Show details便可查閱剛鍵入之資料
轉換至MongoDB中localhost2707目錄下local中startup_log內點擊Refresh即可看到新鍵入之資料或經由刪除後更新的資料資訊

## 專題連結區
- [專題操作影片與版本增修排除問題以及介紹影片](https://youtu.be/lY4q3ExCdFc)
- **期末專題階段性完成日誌**
- **最初構想**
- ● 構想的目標希望建構一個可以供學生進行每學期課程事先安排的預選網站，
- ● 具備系所對應的課程相關資訊(可依學校不同對於靜態資料庫修改)，
- ● 藉由本學期課程中所學習到MySQL以及自學的Dbeaver還有課程中後段學習到的noSQL-mongoDB進行資 料庫的存取。
- ● 透過頁面中對於資料的的新增、編輯與刪除功能，讓使用者進行操作。
- **延伸構想01**
- ● 欲透過下拉式選單讓使用者進行資料階層的選取，致使版面簡潔。
- ● 增能:下拉式選單撰寫，
- ● 連動選單作為使用者可操作的介面進行每學期課程預選擇的活動
- **-開發者日誌 - FinalProject 系列改版紀錄-**

## **FinalProject01fix**
**開發背景：**
- ● 參考課程範例，嘗試實作階層式下拉選單的選課模擬功能，目的是建立一個基礎選課頁面，讓用戶能模擬選擇學院、系所與課程。

**主要進展：**
- ● 成功建置了基礎的階層式下拉選單結構。

**遇到的問題：**
- ● 選課結果無法正確呈現在頁面中。
------------------------------------------
- **FinalProject02fix**
**開發背景：**
- ● 針對 01fix 的結果進行修正與調整，重點在於讓選課結果能夠被正常顯示，初步提升用戶體驗。

**主要進展：**
- ● 新增 selection_result.html，實現選課結果的基本呈現功能。
- ● 初步完成選課功能，能顯示部分選課結果。

**遇到的問題：**
- ● 尚未包含完整的學院、系所與課程資訊。
- ● 修正功能未正常運作，點擊刪除功能時會直接返回選課頁面。
------------------------------------------
- **FinalProject03fix**
**開發背景：**
- ● 擴充學院、系所及課程資訊的完整性，進一步提升功能的實用性。

**主要進展：**
- ● 擴充並補充完整的學院、系所及課程資料，內容更豐富。

**遇到的問題：**
- ● 無法進行多重選課，用戶一次僅能選擇一門課程。

------------------------------------------
- **FinalProject04fix**
**開發背景：**
- ● 著手解決多重選課功能的問題，同時增強使用者互動體驗。

**主要進展：**
- ● 排除無法多重選課的問題，用戶現在可以選擇多門課程。
- ● 新增「選入」按鈕，並在頁面下方設置動態顯示區塊，實時呈現已選課程。
- ● 新增輸入使用者名稱功能，課程選擇結果將按照名稱分類並呈現。

**遇到的問題：**
- ● 結果頁面無法正確跳轉，影響選課體驗的連貫性。
------------------------------------------
- **FinalProject05fix**
**開發背景：**
- ● 集中處理多重選課與資料記錄問題，提升系統穩定性與資料保存能力。

**主要進展：**
- ● 修正多重選課部分的邏輯錯誤，功能已穩定運作。

**遇到的問題：**
- ● 目前僅能顯示單一使用者的選課資料，無法保存過往的選課記錄。
------------------------------------------
- **FinalProject06fix**
**開發背景：**
- ● 解決選課結果顯示的問題，並進一步完善結果資料的操作功能。

**主要進展：**
- ● 修正無法顯示選課結果的問題，用戶現在可正常查看選課結果。
- ● 新增選課結果資料的編輯與刪除功能，用戶可以對已選課程進行調整。
- ● 完善多名用戶資料的記錄機制，過往選課資料不再被覆蓋。

**遇到的問題：**
- ● 刪除使用者選取的所有課程時，僅會留下使用者名稱，導致資料顯示不完整。
------------------------------------------
- **FinalProject07fix (最終版)**
**開發背景：**
- ● 在功能與邏輯上進行最後修正，專注於系統的穩定性與用戶體驗的細節完善。

**主要進展：**
- ● 階層式下拉選單功能完全正常，學院、系所及課程的邏輯切換（如重置下層選項）得以實現。
- ● 使用者名稱設定為必填，未輸入名稱時系統將彈出提示警告。
- ● 增加邏輯設定：當用戶未選擇任何課程時，會自動刪除該使用者的資料，避免冗餘資訊存留。
------------------------------------------
- **未來增修方向**
**版面美化：**
- ● 增加頁面樣式設計，提升系統的視覺吸引力與操作直觀性。

**功能擴充：**
- ● 支援選課時間的設定與檢查（例如：避免衝堂課程）。
- ● 增加課程詳細資訊的展示（例如：學分數、教師資訊、課程描述等）。
- ● 提供選課結果的導出功能（如 PDF 或 Excel 格式）。
- ● 學分的加總功能
