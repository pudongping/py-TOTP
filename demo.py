#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Alex"

import pyotp
import time

# 生成一个密钥（base32 编码）
secret_key = pyotp.random_base32()

# 使用密钥和时间间隔（默认为 30 秒）创建一个 TOTP 对象
totp = pyotp.TOTP(secret_key)

# 生成当前的 TOTP
current_totp = totp.now()
print(f"当前 TOTP: {current_totp}")

# 验证 TOTP 是否有效
is_valid = totp.verify(current_totp)
print(f"TOTP 是否有效？ {is_valid}")

# 为了演示 TOTP 有效性窗口，等待下一个时间间隔
# 因为上面默认的时间间隔设定的是 30 秒，所以这里故意等待 31 秒
time.sleep(31)

# 再次尝试验证 TOTP（由于时间窗口已过，应该无效）
is_valid = totp.verify(current_totp)
print(f"TOTP 仍然有效吗？ {is_valid}")
