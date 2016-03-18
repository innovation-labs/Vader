# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0015_auto_mapping_stripe_to_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('DZD', 'Algerian Dinar'), ('NAD', 'Namibian Dollar'), ('GHS', 'Ghana Cedi'), ('EGP', 'Egyptian Pound'), ('BGN', 'Bulgarian Lev'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XAG', 'Silver'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('DKK', 'Danish Krone'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('BWP', 'Pula'), ('LBP', 'Lebanese Pound'), ('TZS', 'Tanzanian Shilling'), ('VND', 'Dong'), ('AOA', 'Kwanza'), ('KHR', 'Riel'), ('MYR', 'Malaysian Ringgit'), ('KYD', 'Cayman Islands Dollar'), ('LYD', 'Libyan Dinar'), ('UAH', 'Hryvnia'), ('JOD', 'Jordanian Dinar'), ('AWG', 'Aruban Guilder'), ('SAR', 'Saudi Riyal'), ('EUR', 'Euro'), ('HKD', 'Hong Kong Dollar'), ('CHF', 'Swiss Franc'), ('GIP', 'Gibraltar Pound'), ('BYR', 'Belarussian Ruble'), ('ALL', 'Lek'), ('XPD', 'Palladium'), ('MRO', 'Ouguiya'), ('HRK', 'Croatian Kuna'), ('DJF', 'Djibouti Franc'), ('SZL', 'Lilangeni'), ('THB', 'Baht'), ('XAF', 'CFA franc BEAC'), ('BND', 'Brunei Dollar'), ('ISK', 'Iceland Krona'), ('UYU', 'Uruguayan peso'), ('NIO', 'Cordoba Oro'), ('LAK', 'Kip'), ('XYZ', 'Default currency.'), ('SYP', 'Syrian Pound'), ('MAD', 'Moroccan Dirham'), ('MZN', 'Metical'), ('PHP', 'Philippine Peso'), ('ZAR', 'Rand'), ('NPR', 'Nepalese Rupee'), ('ZWL', 'Zimbabwe dollar A/09'), ('ZWN', 'Zimbabwe dollar A/08'), ('NGN', 'Naira'), ('ZWD', 'Zimbabwe Dollar A/06'), ('CRC', 'Costa Rican Colon'), ('AED', 'UAE Dirham'), ('EEK', 'Kroon'), ('MWK', 'Kwacha'), ('LKR', 'Sri Lanka Rupee'), ('SKK', 'Slovak Koruna'), ('PKR', 'Pakistan Rupee'), ('HUF', 'Forint'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('LSL', 'Lesotho loti'), ('MNT', 'Tugrik'), ('AMD', 'Armenian Dram'), ('UGX', 'Uganda Shilling'), ('QAR', 'Qatari Rial'), ('XDR', 'SDR'), ('JMD', 'Jamaican Dollar'), ('GEL', 'Lari'), ('SHP', 'Saint Helena Pound'), ('AFN', 'Afghani'), ('SBD', 'Solomon Islands Dollar'), ('KPW', 'North Korean Won'), ('TRY', 'Turkish Lira'), ('BDT', 'Taka'), ('YER', 'Yemeni Rial'), ('HTG', 'Haitian gourde'), ('XOF', 'CFA Franc BCEAO'), ('MGA', 'Malagasy Ariary'), ('ANG', 'Netherlands Antillian Guilder'), ('LRD', 'Liberian Dollar'), ('RWF', 'Rwanda Franc'), ('NOK', 'Norwegian Krone'), ('MOP', 'Pataca'), ('INR', 'Indian Rupee'), ('MXN', 'Mexixan peso'), ('CZK', 'Czech Koruna'), ('TJS', 'Somoni'), ('BTN', 'Bhutanese ngultrum'), ('COP', 'Colombian peso'), ('MUR', 'Mauritius Rupee'), ('IDR', 'Rupiah'), ('HNL', 'Lempira'), ('XPF', 'CFP Franc'), ('FJD', 'Fiji Dollar'), ('ETB', 'Ethiopian Birr'), ('PEN', 'Nuevo Sol'), ('BZD', 'Belize Dollar'), ('ILS', 'New Israeli Sheqel'), ('DOP', 'Dominican Peso'), ('TMM', 'Manat'), ('TWD', 'New Taiwan Dollar'), ('MDL', 'Moldovan Leu'), ('XPT', 'Platinum'), ('BSD', 'Bahamian Dollar'), ('TVD', 'Tuvalu dollar'), ('SEK', 'Swedish Krona'), ('ZMK', 'Kwacha'), ('MVR', 'Rufiyaa'), ('XTS', 'Codes specifically reserved for testing purposes'), ('AUD', 'Australian Dollar'), ('SRD', 'Surinam Dollar'), ('CUP', 'Cuban Peso'), ('BBD', 'Barbados Dollar'), ('KMF', 'Comoro Franc'), ('KRW', 'Won'), ('GMD', 'Dalasi'), ('VEF', 'Bolivar Fuerte'), ('IMP', 'Isle of Man pount'), ('CUC', 'Cuban convertible peso'), ('CLP', 'Chilean peso'), ('LTL', 'Lithuanian Litas'), ('CDF', 'Congolese franc'), ('XCD', 'East Caribbean Dollar'), ('KZT', 'Tenge'), ('RUB', 'Russian Ruble'), ('XFU', 'UIC-Franc'), ('TTD', 'Trinidad and Tobago Dollar'), ('OMR', 'Rial Omani'), ('BRL', 'Brazilian Real'), ('MMK', 'Kyat'), ('PLN', 'Zloty'), ('PYG', 'Guarani'), ('KES', 'Kenyan Shilling'), ('MKD', 'Denar'), ('GBP', 'Pound Sterling'), ('AZN', 'Azerbaijanian Manat'), ('TOP', 'Paanga'), ('VUV', 'Vatu'), ('GNF', 'Guinea Franc'), ('WST', 'Tala'), ('IQD', 'Iraqi Dinar'), ('ERN', 'Nakfa'), ('BAM', 'Convertible Marks'), ('SCR', 'Seychelles Rupee'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KWD', 'Kuwaiti Dinar'), ('BIF', 'Burundi Franc'), ('PGK', 'Kina'), ('SOS', 'Somali Shilling'), ('SGD', 'Singapore Dollar'), ('UZS', 'Uzbekistan Sum'), ('STD', 'Dobra'), ('XFO', 'Gold-Franc'), ('IRR', 'Iranian Rial'), ('CNY', 'Yuan Renminbi'), ('SLL', 'Leone'), ('TND', 'Tunisian Dinar'), ('GYD', 'Guyana Dollar'), ('NZD', 'New Zealand Dollar'), ('FKP', 'Falkland Islands Pound'), ('LVL', 'Latvian Lats'), ('USD', 'US Dollar'), ('KGS', 'Som'), ('ARS', 'Argentine Peso'), ('RON', 'New Leu'), ('GTQ', 'Quetzal'), ('RSD', 'Serbian Dinar'), ('BHD', 'Bahraini Dinar'), ('JPY', 'Yen'), ('SDG', 'Sudanese Pound'), ('XAU', 'Gold')], default=b'USD', max_length=4),
        ),
        migrations.AddField(
            model_name='plan',
            name='currency',
            field=models.CharField(choices=[('DZD', 'Algerian Dinar'), ('NAD', 'Namibian Dollar'), ('GHS', 'Ghana Cedi'), ('EGP', 'Egyptian Pound'), ('BGN', 'Bulgarian Lev'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XAG', 'Silver'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('DKK', 'Danish Krone'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('BWP', 'Pula'), ('LBP', 'Lebanese Pound'), ('TZS', 'Tanzanian Shilling'), ('VND', 'Dong'), ('AOA', 'Kwanza'), ('KHR', 'Riel'), ('MYR', 'Malaysian Ringgit'), ('KYD', 'Cayman Islands Dollar'), ('LYD', 'Libyan Dinar'), ('UAH', 'Hryvnia'), ('JOD', 'Jordanian Dinar'), ('AWG', 'Aruban Guilder'), ('SAR', 'Saudi Riyal'), ('EUR', 'Euro'), ('HKD', 'Hong Kong Dollar'), ('CHF', 'Swiss Franc'), ('GIP', 'Gibraltar Pound'), ('BYR', 'Belarussian Ruble'), ('ALL', 'Lek'), ('XPD', 'Palladium'), ('MRO', 'Ouguiya'), ('HRK', 'Croatian Kuna'), ('DJF', 'Djibouti Franc'), ('SZL', 'Lilangeni'), ('THB', 'Baht'), ('XAF', 'CFA franc BEAC'), ('BND', 'Brunei Dollar'), ('ISK', 'Iceland Krona'), ('UYU', 'Uruguayan peso'), ('NIO', 'Cordoba Oro'), ('LAK', 'Kip'), ('XYZ', 'Default currency.'), ('SYP', 'Syrian Pound'), ('MAD', 'Moroccan Dirham'), ('MZN', 'Metical'), ('PHP', 'Philippine Peso'), ('ZAR', 'Rand'), ('NPR', 'Nepalese Rupee'), ('ZWL', 'Zimbabwe dollar A/09'), ('ZWN', 'Zimbabwe dollar A/08'), ('NGN', 'Naira'), ('ZWD', 'Zimbabwe Dollar A/06'), ('CRC', 'Costa Rican Colon'), ('AED', 'UAE Dirham'), ('EEK', 'Kroon'), ('MWK', 'Kwacha'), ('LKR', 'Sri Lanka Rupee'), ('SKK', 'Slovak Koruna'), ('PKR', 'Pakistan Rupee'), ('HUF', 'Forint'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('LSL', 'Lesotho loti'), ('MNT', 'Tugrik'), ('AMD', 'Armenian Dram'), ('UGX', 'Uganda Shilling'), ('QAR', 'Qatari Rial'), ('XDR', 'SDR'), ('JMD', 'Jamaican Dollar'), ('GEL', 'Lari'), ('SHP', 'Saint Helena Pound'), ('AFN', 'Afghani'), ('SBD', 'Solomon Islands Dollar'), ('KPW', 'North Korean Won'), ('TRY', 'Turkish Lira'), ('BDT', 'Taka'), ('YER', 'Yemeni Rial'), ('HTG', 'Haitian gourde'), ('XOF', 'CFA Franc BCEAO'), ('MGA', 'Malagasy Ariary'), ('ANG', 'Netherlands Antillian Guilder'), ('LRD', 'Liberian Dollar'), ('RWF', 'Rwanda Franc'), ('NOK', 'Norwegian Krone'), ('MOP', 'Pataca'), ('INR', 'Indian Rupee'), ('MXN', 'Mexixan peso'), ('CZK', 'Czech Koruna'), ('TJS', 'Somoni'), ('BTN', 'Bhutanese ngultrum'), ('COP', 'Colombian peso'), ('MUR', 'Mauritius Rupee'), ('IDR', 'Rupiah'), ('HNL', 'Lempira'), ('XPF', 'CFP Franc'), ('FJD', 'Fiji Dollar'), ('ETB', 'Ethiopian Birr'), ('PEN', 'Nuevo Sol'), ('BZD', 'Belize Dollar'), ('ILS', 'New Israeli Sheqel'), ('DOP', 'Dominican Peso'), ('TMM', 'Manat'), ('TWD', 'New Taiwan Dollar'), ('MDL', 'Moldovan Leu'), ('XPT', 'Platinum'), ('BSD', 'Bahamian Dollar'), ('TVD', 'Tuvalu dollar'), ('SEK', 'Swedish Krona'), ('ZMK', 'Kwacha'), ('MVR', 'Rufiyaa'), ('XTS', 'Codes specifically reserved for testing purposes'), ('AUD', 'Australian Dollar'), ('SRD', 'Surinam Dollar'), ('CUP', 'Cuban Peso'), ('BBD', 'Barbados Dollar'), ('KMF', 'Comoro Franc'), ('KRW', 'Won'), ('GMD', 'Dalasi'), ('VEF', 'Bolivar Fuerte'), ('IMP', 'Isle of Man pount'), ('CUC', 'Cuban convertible peso'), ('CLP', 'Chilean peso'), ('LTL', 'Lithuanian Litas'), ('CDF', 'Congolese franc'), ('XCD', 'East Caribbean Dollar'), ('KZT', 'Tenge'), ('RUB', 'Russian Ruble'), ('XFU', 'UIC-Franc'), ('TTD', 'Trinidad and Tobago Dollar'), ('OMR', 'Rial Omani'), ('BRL', 'Brazilian Real'), ('MMK', 'Kyat'), ('PLN', 'Zloty'), ('PYG', 'Guarani'), ('KES', 'Kenyan Shilling'), ('MKD', 'Denar'), ('GBP', 'Pound Sterling'), ('AZN', 'Azerbaijanian Manat'), ('TOP', 'Paanga'), ('VUV', 'Vatu'), ('GNF', 'Guinea Franc'), ('WST', 'Tala'), ('IQD', 'Iraqi Dinar'), ('ERN', 'Nakfa'), ('BAM', 'Convertible Marks'), ('SCR', 'Seychelles Rupee'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KWD', 'Kuwaiti Dinar'), ('BIF', 'Burundi Franc'), ('PGK', 'Kina'), ('SOS', 'Somali Shilling'), ('SGD', 'Singapore Dollar'), ('UZS', 'Uzbekistan Sum'), ('STD', 'Dobra'), ('XFO', 'Gold-Franc'), ('IRR', 'Iranian Rial'), ('CNY', 'Yuan Renminbi'), ('SLL', 'Leone'), ('TND', 'Tunisian Dinar'), ('GYD', 'Guyana Dollar'), ('NZD', 'New Zealand Dollar'), ('FKP', 'Falkland Islands Pound'), ('LVL', 'Latvian Lats'), ('USD', 'US Dollar'), ('KGS', 'Som'), ('ARS', 'Argentine Peso'), ('RON', 'New Leu'), ('GTQ', 'Quetzal'), ('RSD', 'Serbian Dinar'), ('BHD', 'Bahraini Dinar'), ('JPY', 'Yen'), ('SDG', 'Sudanese Pound'), ('XAU', 'Gold')], default=b'USD', max_length=4),
        ),
    ]