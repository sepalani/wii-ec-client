#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""EC utils module.

    Wii EC Client Project
    Copyright (C) 2018  Sepalani

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests
import ConfigParser


class Config(object):
    def __init__(self, filename="ec.cfg"):
        cfg = ConfigParser.RawConfigParser()
        cfg.read(filename)
        # Wii certificates
        self.client_crt = cfg.get("Wii", "ClientCA")
        self.client_key = cfg.get("Wii", "ClientCAKey")
        self.root_ca = cfg.get("Wii", "RootCA")
        self.device_cert = cfg.get("Wii", "DeviceCert")
        # Wii properties
        self.device_id = cfg.get("Wii", "DeviceId")
        self.account_id = cfg.get("Wii", "AccountId")
        self.region = cfg.get("Wii", "Region")
        self.country = cfg.get("Wii", "Country")
        self.language = cfg.get("Wii", "Language")
        self.serial_no = cfg.get("Wii", "SerialNo")
        # ECDK properties
        self.ecdk_version = cfg.get("ECDK", "Version")
        self.ecdk_user_agent = cfg.get("ECDK", "User-Agent")
        self.ecdk_ec_version = cfg.get("ECDK", "ECVersion")
        self.tin = cfg.get("ECDK", "TIN")
        self.application_id = cfg.get("ECDK", "ApplicationId")
        # ECSHOP properties
        self.ecshop_version = cfg.get("ECSHOP", "Version")
        self.ecshop_user_agent = cfg.get("ECSHOP", "User-Agent")


def send_ecdk(url, soap, action, cfg):
    headers = {
        "User-Agent": cfg.ecdk_user_agent,
        "Accept": "application/xml",
        "Accept-Charset": "UTF-8",
        "Content-type": "text/xml; charset=utf-8",
        "SOAPAction": action
    }
    return requests.post(
        url,
        cert=(cfg.client_crt, cfg.client_key),
        verify=cfg.root_ca,
        data=soap, headers=headers
    )


def send_ecshop(url, soap, action, cfg):
    headers = {
        "User-Agent": cfg.ecshop_user_agent,
        "Accept": "application/xml",
        "Accept-Charset": "UTF-8",
        "Content-type": "text/xml; charset=utf-8",
        "SOAPAction": action
    }
    return requests.post(
        url,
        cert=(cfg.client_crt, cfg.client_key),
        verify=cfg.root_ca,
        data=soap, headers=headers
    )


if __name__ == "__main__":
    cfg = Config("ec.cfg")
    for k in dir(cfg):
        if "_" == k[:1]:
            continue
        print("{} = {}".format(k, getattr(cfg, k)))
