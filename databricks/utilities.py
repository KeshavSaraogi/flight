def insert_test_cases(database,insert_id,insert_test_cases,insert_test_query,insert_expected_result):
    try:
        spark.sql(f"""create table if not exists {database}.insert_test_cases(
                 id int,
                 test_cases string,
                 test_query string,
                 expected_result int

        )""")
        spark.sql(f"""insert into {database}.insert_test_cases(id,test_cases,test_query,expected_result) values({insert_id},'{insert_test_cases}','{insert_test_query}',{insert_expected_result})""")
    except Exception as err:
        print("Error occurred", str(err))


def excecute_test_case(database):
    df=spark.sql(f"""select * from {database}.insert_test_cases """).collect()
    for i in df:
        orginal_result=spark.sql(f"""{i.test_query}""").collect()
        if(len(orginal_result)==i.expected_result):
            print("Test case is passed")
        else:
            raise Exception (f"{test_cases} is failed, Kindly check")

def pre_schema(location):
    try:
        df=spark.read.format('delta').load(f'{location}').limit(1)
        schema=""
        for i in df.dtypes:
           schema=schema+i[0]+" "+i[1]+","
        return schema[0:-1]
    except Exception as err:
        print("Error Ocurred ",str(err))
