# Changelog
All notable changes to **Recycling Meltspinning Materials Calculator** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2025-12-05
### Added
- Initial release of the Recycling Meltspinning Materials Calculator
- GUI with entry/result fields for Oil, PSU, SPC, SKPC, Flake, Chips, Master batch, Waste, Bunker mass
- Master batch mode toggle (kg / %)
- Flake mix strategy with two flake rows and checkbox
- Help → About menu with author info, license, version, and GitHub link
- Calculate and Reset buttons

---

## [1.1.0] - 2026-01-15
### Added
- Improved Reset function to clear all fields consistently
- Enhanced Flake mix logic with validation for percentages (1–99)
- Default reset for Master batch mode (kg)

### Fixed
- Bug where Bunker mass result box caused errors
- KeyError when accessing Flake entry from dictionary

---

## [1.2.0] - 2026-02-20
### Added
- Status bar showing calculation state (“Ready”, “Calculated at …”)
- Error handling for invalid inputs (non-numeric values)

### Changed
- Updated About window text to consistently use “Materials”
- Improved layout for Flake rows (placed before Chips)

---

## [Unreleased]
### Planned
- Export results to CSV/Excel
- Change the formula for Pelt and Chips
- Dark mode UI option
