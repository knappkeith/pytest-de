
## pytest commands:

1 - Fixtures and Folder Structure simple test

```bash
pytest tests/db_tests/addr/test_addr_landing.py -vv
```

2 - Common TestClass for users

```bash
pytest tests/db_tests/users/test_users_staging.py -vv
```

3 - Smoke Marker

```bash
pytest tests/db_tests/orders -m smoke -vv
```

4 - Landing Marker

```bash
pytest tests/db_tests/orders -m landing -vv
```

5 - Skipif Tests

```bash
pytest tests/db_tests/orders/test_orders_landing.py -vv
```

6 - Xfail tests

```bash
pytest tests/db_tests/orders/test_orders_staging.py -vv
```