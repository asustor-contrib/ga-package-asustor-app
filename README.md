# Package Asustor App

The `asustor-contrib/ga-package-asustor-app` action is a Docker action that runs 
[apkg-tools.py](https://developer.asustor.com/document/APKG_Utilities_2.0.zip) to create an apkg bundle.

After you've used the action, subsequent steps in the same job can work with the generated *.apk file.

## Usage

```yaml
    steps:
      # ...
      - id: package_asustor_app
        name: Package Asustor App
        uses: asustor-contrib/ga-package-asustor-app@v2
        with:
          apkg-dir: 'asustor_package'
          out-dir: 'out'
      # ...
```

## Inputs

- `apkg-dir`: (**Required**) Package directory. Defaults to `"package"`.

Expected directory structure:
```plain
├── bin
│  └── dlcd
├── CONTROL
│  ├── config.json
│  ├── icon.png
│  ├── license.txt
│  ├── decription.txt
│  ├── changlog.txt
│  ├── post-install.sh
│  ├── post-uninstall.sh
│  ├── pre-install.sh
│  ├── pre-uninstall.sh
│  ├── start-stop.sh
│  ├── pre-snapshot-restore.sh
│  └── post-snapshot-restore.sh
├── etc
│  ├── plugin
│  │  ├── rss.json
│  │  └── search.json
│  └── settings.json
├── lib
│  ├── libdlcenter.so -> libdlcenter.so.0.0
│  ├── libdlcenter.so.0 -> libdlcenter.so.0.0
│  ├── libdlcenter.so.0.0
│  ├── libevent-2.0.so.5 -> libevent-2.0.so.5.1.1
│  └── libevent-2.0.so.5.1.1 
└── webman
   ├── dlcenter.cgi
   ├── downloadCenter.js
   ├── images
   │  ├── icon-app-task.png
   │  ├── icon.png
   │  ├── icon-title.png
   │  ├── left_icon1.png
   └── langs
      └── lang-en-US.js
```

- `out-dir`: (**Required**) Destination Directory. Defaults to `"."`.

## Outputs

- `apkg-app-info-general-package`: Bundled Asustor Package.
  
- `apkg-app-info-general-name`: Bundled Asustor Package Name.
  
- `apkg-app-info-general-version`: Bundled Asustor Package Version.
  
- `apkg-app-info-general-developer`: Bundled Asustor Package Developer.
  
- `apkg-app-info-general-maintainer`: Bundled Asustor Package Maintainer.
  
- `apkg-app-info-general-email`: Bundled Asustor Package Maintainer Email.
  
- `apkg-app-info-general-website`: Bundled Asustor Package Website.
  
- `apkg-app-info-general-architecture`: Bundled Asustor Package Architecture.
  
- `apkg-app-info-general-firmware`: Bundled Asustor Package Firmware.
  
- `apkg-file-name`: Bundled Asustor Package File Name.
  
- `apkg-file-path`: Bundled Asustor Package File Path.

## Resources

[Asustor Developer Center](https://developer.asustor.com/developerCenter)

[Asustor App Central Developer Guide (3.5.0_20200923)](http://download.asustor.com/developer/App_Central_Developer_Guide_3.5.0_20200923.pdf)

[Asustor App Build Tools (APKG_Utilities_2.0)](https://developer.asustor.com/document/APKG_Utilities_2.0.zip)

[Upload your Asustor Application](https://developer.asustor.com/document/Upload%20your%20Application.pdf)
