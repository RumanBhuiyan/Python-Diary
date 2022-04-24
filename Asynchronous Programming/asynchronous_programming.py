import asyncio
import requests

async def fetch_users():
    response = requests.get('https://www.testjsonapi.com/users/')
    users = response.json()
    
    for user in users :
        print(f"name :{user['name']} email : {user['email']}")
    return users

async def user():
    # process-01: below line will block execution of print statement untill it ends
    # await fetch_users()
    # print("Users fetching........")

    # process-02 : below 2 lines will block execution of print statement untill they end
    # users = asyncio.create_task(fetch_users())
    # await users
    # print("Users fetching........")

    # process-03 : we can manually tell how much time it need to wait like below
    #await asyncio.sleep(1)

    # process-04  : below line wont block executing print statement before it ends
    response = asyncio.create_task(fetch_users())
    print("Users fetching........")
    users = await response # because i dont want to print users before receiving users
    print(f"Users are : {users}")

# asyncio.run() is used to call asynchronous function and  await is used
# only inside async function like as javascript. In python await is used before
# the variable which is an asynchronous task.asyncio block execution of print before it finishes
asyncio.run(user())
print('Asynchronous Programming..........')
