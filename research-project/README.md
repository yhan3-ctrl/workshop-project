# Course workshop project

These materials support a short course workshop review. The team collected
weekly attendance counts, summarized discussion points, and drafted a report.
All names, counts, and project details in this workspace are fictional.

Raw exports are in `data/raw/`. Draft report versions, meeting notes, derived
tables, and room materials are currently spread across several folders.

## Weekly attendance summary

From this folder, run:

```sh
python scripts/build_summary.py
```

The script reads `data/raw/attendance_week1.csv` and
`data/raw/attendance_week2.csv` relative to this folder and prints weekly
registration and attendance totals. It does not write any files. Attendance
counts are session visits, not unique people.
