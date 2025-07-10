-- テーブルの作成
CREATE TABLE MEAL(id int not null primary key, name varchar(100));

-- テーブルにデータを挿入
INSERT INTO MEAL VALUES(1, 'Sushi');
INSERT INTO MEAL VALUES(2, 'Yakiniku');
INSERT INTO MEAL VALUES(3, 'Soba');
INSERT INTO MEAL VALUES(4, 'Okonomiyaki');

-- テーブルを表示
SELECT * FROM MEAL;


