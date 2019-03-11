# -*- coding: utf-8 -*-
# Copyright 2009-2019 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Belgium - Multilingual Chart of Accounts (en/nl/fr)',
    'version': '8.0.1.9.2',
    'license': 'AGPL-3',
    'author': "Noviat, Odoo Community Association (OCA)",
    'website': 'http://www.noviat.com',
    'category': 'Localization/Account Charts',
    'summary': 'Belgium - Multilingual Chart of Accounts (en/nl/fr)',
    'depends': [
        'base_vat',
        'base_iban',
        'account_chart',
    ],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'data/account_account_type_nov.xml',
        'data/account_account_template_nov.xml',
        'data/account_tax_code_template_nov.xml',
        'data/account_chart_template_nov.xml',
        'data/account_tax_template_nov.xml',
        'data/account_fiscal_position_template_nov.xml',
        'data/account_fiscal_position_tax_template_nov.xml',
        'data/account_fiscal_position_account_template_nov.xml',
        'data/account_financial_report.xml',
        'data/be_legal_financial_reportscheme.xml',
        'data/l10n_be_sequence.xml',
        'views/account_menuitem.xml',
        'views/account_view.xml',
        'views/account_financial_report_view.xml',
        'views/res_config_view.xml',
        'views/l10n_be_layouts.xml',
        'views/report_financial.xml',
        'views/report_l10nbevatdeclaration.xml',
        'views/report_l10nbevatlisting.xml',
        'views/report_l10nbevatintra.xml',
        'wizard/wizard_multi_charts_accounts.xml',
        'wizard/l10n_be_update_be_reportscheme.xml',
        'wizard/reports.xml',
        'wizard/l10n_be_vat_declaration_view.xml',
        'wizard/l10n_be_vat_intra_view.xml',
        'wizard/l10n_be_partner_vat_listing.xml',
    ],
    'installable': True,
}
