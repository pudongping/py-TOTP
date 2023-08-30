#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Alex"

import pyotp
import sys


def get_current_totp(secret):
    '''
    获取此时的TOTP
    :param secret:
    :return:
    '''

    totp = pyotp.TOTP(secret)
    return totp.now()


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 %s <secret>" % args[0])
        sys.exit(1)

    secret = args[1]
    print(f"此时的 TOTP 为：{get_current_totp(secret)}")


if __name__ == "__main__":
    main()
