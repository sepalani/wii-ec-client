#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""ECDK module.

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

import EC


def check_device_status(cfg,
                        message_id="12345678901234567",
                        device_token="123456789abcdef0123456789abcdef0"):
    soap = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:ecs="urn:ecs.wsapi.broadon.com">
<SOAP-ENV:Body>
<ecs:CheckDeviceStatus xsi:type="ecs:CheckDeviceStatusRequestType">
  <ecs:Version>{cfg.ecdk_version}</ecs:Version>
  <ecs:MessageId>ECDK-{cfg.device_id}-{message_id}</ecs:MessageId>
  <ecs:DeviceId>{cfg.device_id}</ecs:DeviceId>
  <ecs:DeviceToken>WT-{device_token}</ecs:DeviceToken>
  <ecs:AccountId>{cfg.account_id}</ecs:AccountId>
  <ecs:ApplicationId>{cfg.application_id}</ecs:ApplicationId>
  <ecs:TIN>{cfg.tin}</ecs:TIN>
  <ecs:Region>{cfg.region}</ecs:Region>
  <ecs:Country>{cfg.country}</ecs:Country>
  <ecs:Language>{cfg.language}</ecs:Language>
  <ecs:SerialNo>{cfg.serial_no}</ecs:SerialNo>
</ecs:CheckDeviceStatus>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>""".format(cfg=cfg,
                               message_id=message_id,
                               device_token=device_token)
    return EC.send_ecdk(
        "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP", soap,
        "urn:ecs.wsapi.broadon.com/CheckDeviceStatus", cfg
    )


def get_ec_config(cfg,
                  message_id="12345678901234567",
                  device_token="123456789abcdef0123456789abcdef0"):
    soap = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:ecs="urn:ecs.wsapi.broadon.com">
<SOAP-ENV:Body>
<ecs:GetECConfig xsi:type="ecs:GetECConfigRequestType">
  <ecs:Version>{cfg.ecdk_version}</ecs:Version>
  <ecs:MessageId>ECDK-{cfg.device_id}-{message_id}</ecs:MessageId>
  <ecs:DeviceId>{cfg.device_id}</ecs:DeviceId>
  <ecs:DeviceToken>WT-{device_token}</ecs:DeviceToken>
  <ecs:AccountId>{cfg.account_id}</ecs:AccountId>
  <ecs:ApplicationId>{cfg.application_id}</ecs:ApplicationId>
  <ecs:TIN>{cfg.tin}</ecs:TIN>
  <ecs:Region>{cfg.region}</ecs:Region>
  <ecs:Country>{cfg.country}</ecs:Country>
  <ecs:Language>{cfg.language}</ecs:Language>
  <ecs:SerialNo>{cfg.serial_no}</ecs:SerialNo>
  <ecs:ECVersion>{cfg.ecdk_ec_version}</ecs:ECVersion>
</ecs:GetECConfig>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>""".format(cfg=cfg,
                               message_id=message_id,
                               device_token=device_token)
    return EC.send_ecdk(
        "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP", soap,
        "urn:ecs.wsapi.broadon.com/GetECConfig", cfg
    )


def list_titles(cfg,
                message_id="12345678901234567",
                device_token="123456789abcdef0123456789abcdef0"):
    soap = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:cas="urn:cas.wsapi.broadon.com">
<SOAP-ENV:Body>
<cas:ListTitles xsi:type="cas:ListTitlesRequestType">
  <cas:Version>{cfg.ecdk_version}</cas:Version>
  <cas:MessageId>ECDK-{cfg.device_id}-{message_id}</cas:MessageId>
  <cas:DeviceId>{cfg.device_id}</cas:DeviceId>
  <cas:DeviceToken>WT-{device_token}</cas:DeviceToken>
  <cas:AccountId>{cfg.account_id}</cas:AccountId>
  <cas:ApplicationId>{cfg.application_id}</cas:ApplicationId>
  <cas:TIN>{cfg.tin}</cas:TIN>
  <cas:Region>{cfg.region}</cas:Region>
  <cas:Country>{cfg.country}</cas:Country>
  <cas:Language>{cfg.language}</cas:Language>
  <cas:ListResultOffset>0</cas:ListResultOffset>
  <cas:ListResultLimit>40</cas:ListResultLimit>
  <cas:Attributes>Prices</cas:Attributes>
  <cas:Attributes>MaxUserFileSize</cas:Attributes>
  <cas:Attributes>MaxUserInodes</cas:Attributes>
</cas:ListTitles>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>""".format(cfg=cfg,
                               message_id=message_id,
                               device_token=device_token)
    return EC.send_ecdk(
        "https://cas.shop.wii.com/cas/services/CatalogingSOAP", soap,
        "urn:cas.wsapi.broadon.com/ListTitles", cfg
    )


def purchase_title(title_id, item_id, cfg,
                   message_id="12345678901234567",
                   device_token="Ab3dEF/gHIjKLMnoPqrST"):
    soap = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:ecs="urn:ecs.wsapi.broadon.com">
<SOAP-ENV:Body>
<ecs:PurchaseTitle xsi:type="ecs:PurchaseTitleRequestType">
  <ecs:Version>{cfg.ecdk_version}</ecs:Version>
  <ecs:MessageId>ECDK-{cfg.device_id}-{message_id}</ecs:MessageId>
  <ecs:DeviceId>{cfg.device_id}</ecs:DeviceId>
  <ecs:DeviceToken>ST-{device_token}</ecs:DeviceToken>
  <ecs:AccountId>{cfg.account_id}</ecs:AccountId>
  <ecs:ApplicationId>{cfg.application_id}</ecs:ApplicationId>
  <ecs:TIN>{cfg.tin}</ecs:TIN>
  <ecs:Region>{cfg.region}</ecs:Region>
  <ecs:Country>{cfg.country}</ecs:Country>
  <ecs:Language>{cfg.language}</ecs:Language>
  <ecs:SerialNo>{cfg.serial_no}</ecs:SerialNo>
  <ecs:ItemId>{item_id}</ecs:ItemId>
  <ecs:Price>
    <ecs:Amount>0</ecs:Amount>
    <ecs:Currency>POINTS</ecs:Currency>
  </ecs:Price>
  <ecs:Payment>
    <ecs:PaymentMethod>ACCOUNT</ecs:PaymentMethod>
    <ecs:AccountPayment>
      <ecs:AccountNumber>{cfg.account_id}</ecs:AccountNumber>
      <ecs:DeviceToken>{device_token}</ecs:DeviceToken>
    </ecs:AccountPayment>
  </ecs:Payment>
  <ecs:DeviceCert>{cfg.device_cert}</ecs:DeviceCert>
  <ecs:TitleId>{title_id}</ecs:TitleId>
  <ecs:Limits>
    <ecs:Limits>0</ecs:Limits>
    <ecs:LimitKind>PR</ecs:LimitKind>
  </ecs:Limits>
  <ecs:Age>20</ecs:Age>
</ecs:PurchaseTitle>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>""".format(title_id=title_id, item_id=item_id, cfg=cfg,
                               message_id=message_id,
                               device_token=device_token)
    return EC.send_ecdk(
        "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP", soap,
        "urn:ecs.wsapi.broadon.com/PurchaseTitle", cfg
    )

if __name__ == "__main__":
    cfg = EC.Config("ec.cfg")
