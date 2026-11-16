#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ویلہ — تاریخ اور وقت (تینوں زبانیں)"""

from datetime import datetime, timedelta, date
import time as _time


def اب() -> str:
    """ابھی کا وقت (YYYY-MM-DD HH:MM:SS)"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def آج() -> str:
    """آج کی تاریخ (YYYY-MM-DD)"""
    return date.today().strftime("%Y-%m-%d")


def سال() -> int:
    """موجودہ سال"""
    return datetime.now().year


def مہینہ() -> int:
    """موجودہ مہینہ (1-12)"""
    return datetime.now().month


def دن() -> int:
    """موجودہ دن (1-31)"""
    return datetime.now().day


def گھنٹہ() -> int:
    """موجودہ گھنٹہ (0-23)"""
    return datetime.now().hour


def منٹ() -> int:
    """موجودہ منٹ (0-59)"""
    return datetime.now().minute


def سیکنڈ() -> int:
    """موجودہ سیکنڈ (0-59)"""
    return datetime.now().second


def فارمیٹ(فارمیٹ_سٹرنگ: str = "%Y-%m-%d") -> str:
    """وقت کو مخصوص فارمیٹ میں"""
    return datetime.now().strftime(فارمیٹ_سٹرنگ)


def سو_جاؤ(سیکنڈ: int):
    """سو جاؤ (سیکنڈ)"""
    _time.sleep(سیکنڈ)


def فرق_دن(تاریخ_1: str, تاریخ_2: str) -> int:
    """دو تاریخوں کے درمیان دن"""
    d1 = datetime.strptime(تاریخ_1, "%Y-%m-%d")
    d2 = datetime.strptime(تاریخ_2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def شامل_دن(تاریخ: str, دن: int) -> str:
    """تاریخ میں دن شامل کریں"""
    d = datetime.strptime(تاریخ, "%Y-%m-%d")
    return (d + timedelta(days=دن)).strftime("%Y-%m-%d")
