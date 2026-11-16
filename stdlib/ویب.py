#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ویب — HTTP requests، سادہ سرور (تینوں زبانیں)"""

import urllib.request
import urllib.parse
import json


def حاصل_کرو(url: str, ہیڈرز: dict = None) -> str:
    """GET request — ویب صفحہ حاصل کریں"""
    req = urllib.request.Request(url)
    if ہیڈرز:
        for key, value in ہیڈرز.items():
            req.add_header(key, value)
    
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")


def بھیجو(url: str, ڈیٹا: dict = None, ہیڈرز: dict = None) -> str:
    """POST request — ڈیٹا بھیجیں"""
    if ڈیٹا is None:
        ڈیٹا = {}
    
    encoded = urllib.parse.urlencode(ڈیٹا).encode("utf-8")
    req = urllib.request.Request(url, data=encoded, method="POST")
    
    if ہیڈرز:
        for key, value in ہیڈرز.items():
            req.add_header(key, value)
    
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")


def json_حاصل_کرو(url: str) -> dict:
    """JSON API سے ڈیٹا حاصل کریں"""
    response = حاصل_کرو(url, ہیڈرز={"Accept": "application/json"})
    return json.loads(response)


def json_بھیجو(url: str, ڈیٹا: dict) -> dict:
    """JSON API کو ڈیٹا بھیجیں"""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = json.dumps(ڈیٹا).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))
