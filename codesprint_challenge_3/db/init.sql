DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS employees_histories;
DROP TABLE IF EXISTS companies;

-- 最新の社員情報を格納するテーブル
CREATE TABLE employees (
  id integer PRIMARY KEY AUTOINCREMENT, -- 社員ID
  name text NOT NULL,                   -- 氏名
  boss_id integer,                      -- 上司のID ※ NULL の場合は社長
  company_id integer NOT NULL,          -- 勤務先の会社ID
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 過去・現在のすべての社員の異動情報を保持するテーブル
CREATE TABLE employees_histories (
  start_year integer NOT NULL,  -- 開始年
  start_month integer NOT NULL, -- 　　月
  end_year integer,             -- 終了年 ※ NULL の場合は現在も有効なデータ
  end_month integer,            -- 　　月 ※ 同上
  employee_id integer,
  boss_id integer,
  company_id integer NOT NULL,
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- グループの親会社・子会社の情報を格納するテーブル
CREATE TABLE companies (
  id integer PRIMARY KEY AUTOINCREMENT, -- 会社ID
  name text NOT NULL,                   -- 会社名
  location text NOT NULL,               -- 所在地
  category text NOT NULL                -- 業務区分
);