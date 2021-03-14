#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import os

from apkg_tools import Apkg

if __name__ == "__main__":
    # create the top-level parser
    parser = argparse.ArgumentParser(description='asustor package helper.')

    subparsers = parser.add_subparsers(help='sub-commands')

    # create the parser for the "create" command
    parser_create = subparsers.add_parser('create', help='create package from folder')
    parser_create.add_argument('folder', help='select a package layout folder to pack')
    parser_create.add_argument('--destination', help='move apk to destination folder')
    parser_create.set_defaults(command='create')

    # parsing arguments
    args = parser.parse_args()

    # process commands
    apkg = Apkg()

    if args.command == 'create':
        pkg, app_info = apkg.create(args.folder, args.destination)
        if isinstance(pkg, basestring):
            print("Generated file...")
            print("::set-output name=apkg-file-name::" + os.path.basename(pkg))
            print("::set-output name=apkg-file-path::" + os.path.normpath(args.destination + "/" + os.path.basename(pkg)))
            print("::set-output name=apkg-app-info-general-package::" + app_info['general']['package'])
            print("::set-output name=apkg-app-info-general-name::" + app_info['general']['name'])
            print("::set-output name=apkg-app-info-general-version::" + app_info['general']['version'])
            print("::set-output name=apkg-app-info-general-developer::" + app_info['general']['developer'])
            print("::set-output name=apkg-app-info-general-maintainer::" + app_info['general']['maintainer'])
            print("::set-output name=apkg-app-info-general-email::" + app_info['general']['email'])
            print("::set-output name=apkg-app-info-general-website::" + app_info['general']['website'])
            print("::set-output name=apkg-app-info-general-architecture::" + app_info['general']['architecture'])
            print("::set-output name=apkg-app-info-general-firmware::" + app_info['general']['firmware'])
        else:
            print("Error making package")
