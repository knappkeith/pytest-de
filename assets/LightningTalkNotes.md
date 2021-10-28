* organization is important
  * you need to keep test names/fixtures/configurations/class/file names organized, pick a naming convention and stick to it
  * with massive scale of tests and how easy it is to add possibily 100s or 1000s of tests with 10 lines of code
  * commenting and annotations will help a lot more than you think
  * future you will thank past you, trust me






pytest commands:

1 - Fixtures and Folder Structure simple test

pytest tests/db_tests/addr/test_addr_landing.py -vv

2 - Common TestClass for users

pytest tests/db_tests/users/test_users_staging.py -vv

3 - Smoke Marker

pytest tests/db_tests/orders -m smoke -vv

4 - Landing Marker

pytest tests/db_tests/orders -m landing -vv

5 - Skipif Tests

pytest tests/db_tests/orders/test_orders_landing.py -vv

6 - Xfail tests

pytest tests/db_tests/orders/test_orders_staging.py -vv