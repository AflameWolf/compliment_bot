from parser import adding_site_to_database
from aiogram import executor
from DB import mongo_removal_all_data
from Bot2 import dp


# url ="https://love.romanticcollection.ru/blog/500-trogatelnyh-komplimentov-devushke/"


def main():
    print("run a bot or parser(b/p)")
    start = input()
    if start == "b":
        executor.start_polling(dp, skip_updates=True)
    elif start == "p":
        parser()
        print("run a bot(y/n):")
        answer = input()
        if answer == "y":
            executor.start_polling(dp, skip_updates=True)
    else:
        print("Check if the input is correct")
        main()


def parser():
    print("Link:")
    url=input()
    print("Clear database before starting?(y/n):")
    answer = input()
    if answer == "y":
        mongo_removal_all_data()
    print("Parse multiple pages?(y/n)")
    answer = input()
    if answer == "y":
        print("Ending before pagination:")
        page_name = input()
        print("Start page:")
        page_start = int(input())
        print("Last page:")
        page_end = int(input())
        adding_site_to_database(url, page_name, page_start, page_end)
    else:
        adding_site_to_database(url)


if __name__ == "__main__":
    main()