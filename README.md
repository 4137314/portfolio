# Project portfolio

Electronic engineering student based in Trento, Italy. This repository is the source of truth for the public project index. Add or edit projects in the `portfolio-projects` JSON block below; the site generator groups entries by `category` and displays their `tags` as portfolio metadata. The website refreshes from this repository automatically every six hours.

## Project metadata

Edit this list to add projects. Required fields: `title`, `category` (`University`, `Personal`, or `Engineering & systems`), `description`, `tags`, and `source`. Optional `brief` links to a project page on the website.

<!-- portfolio-projects:begin -->
```json
[
  {"title":"RISC-V CPU core","category":"University","description":"VHDL RV32IM/Zicsr processor with single-cycle and pipelined implementations, verification, and FPGA flows.","tags":["Computer architecture","VHDL","FPGA"],"source":"https://github.com/4137314/RISC-V","brief":"https://4137314.github.io/projects/risc-v/"},
  {"title":"Runtime-reconfigurable CGRA","category":"University","description":"Coarse-grained reconfigurable array with a host tool, emulator, configuration language, and hardware flows.","tags":["FPGA","Digital design"],"source":"https://github.com/4137314/ald-cgra","brief":"https://4137314.github.io/projects/ald-cgra/"},
  {"title":"RP2040 telemetry logger","category":"University","description":"Firmware for GPS and environmental telemetry, persistent logging, USB mass storage, and an OLED interface.","tags":["Embedded systems","C/C++","RP2040"],"source":"https://github.com/4137314/ppse-lab-firmware","brief":"https://4137314.github.io/projects/ppse-firmware/"},
  {"title":"Power supply emulator","category":"University","description":"KiCad schematic and PCB project for emulating power-supply circuits during testing and prototyping.","tags":["Hardware","KiCad","Electronics"],"source":"https://github.com/4137314/ppse-hardware","brief":"https://4137314.github.io/projects/ppse-hardware/"},
  {"title":"Lean synthesis project","category":"Personal","description":"Lean 4 frontend and semantic IR for typed engineering models, properties, and machine-checked proofs.","tags":["Formal methods","Lean 4"],"source":"https://github.com/4137314/synthesis","brief":"https://4137314.github.io/projects/synthesis/"},
  {"title":"Cerebro","category":"Personal","description":"A plain-text mathematics knowledge base with reproducible Org-mode workflows and parametric LaTeX exports.","tags":["Knowledge systems","Org-mode","LaTeX"],"source":"https://github.com/4137314/cerebro","brief":"https://4137314.github.io/projects/cerebro/"},
  {"title":"Terminal retro games","category":"Personal","description":"Modular C and ncurses collection of classic games, built with GNU Autotools.","tags":["Systems programming","C","ncurses"],"source":"https://github.com/4137314/retro-games","brief":"https://4137314.github.io/projects/retro-games/"},
  {"title":"Linux dotfiles","category":"Personal","description":"Personal configuration files for Linux shells, editors, terminal tools, Git, and other utilities.","tags":["Linux","Shell","Developer tooling"],"source":"https://github.com/4137314/.dotfiles"},
  {"title":"NixOS configuration","category":"Engineering & systems","description":"Declarative NixOS configuration for a workstation and local NAS, including development tools, networking, storage, and services.","tags":["Linux","NixOS","Infrastructure"],"source":"https://github.com/4137314/nixos-config","brief":"https://4137314.github.io/projects/nixos-config/"},
  {"title":"HackerOne bug bounty workspace","category":"Engineering & systems","description":"A reproducible Nix-based workspace for authorized programs, with scope-aware workflows and a local PostgreSQL-backed tool.","tags":["Developer tooling","Nix","Security"],"source":"https://github.com/4137314/hack-workspace","brief":"https://4137314.github.io/projects/hack-workspace/"},
  {"title":"USB FPGA development board","category":"Engineering & systems","description":"An ECP5-based USB-form-factor hardware development platform. The repository currently contains the KiCad design files.","tags":["Hardware","FPGA","ECP5","KiCad"],"source":"https://github.com/4137314/usb-lab"}
]
```
<!-- portfolio-projects:end -->

## Contact

[Contact me](mailto:mattia.fait.eng@gmail.com) · [LinkedIn](https://www.linkedin.com/in/mattia-f-402062447)
