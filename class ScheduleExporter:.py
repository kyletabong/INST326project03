import calendar

class ScheduleExporter:
    @staticmethod
    def export_to_html(schedule, year, month):
        # Start building the HTML string for the schedule
        html_schedule = f"""
        <html>
        <head>
            <title>Care Schedule for {calendar.month_name[month]} {year}</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Care Schedule for {calendar.month_name[month]} {year}</h1>
            <table>
                <tr>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
        """

        # Get the first weekday and total number of days in the month
        first_weekday, num_days = calendar.monthrange(year, month)
        current_day = 1

        # Build the schedule table rows
        for week in range((num_days + first_weekday + 6) // 7):  # Ensure it accounts for partial weeks
            html_schedule += "<tr>"
            for day in range(7):  # Iterate over the 7 days of the week
                if (week == 0 and day < first_weekday) or current_day > num_days:
                    # Add an empty cell for days before the start of the month or after the month's end
                    html_schedule += "<td></td>"
                else:
                    # Retrieve shifts for the current day or default to "Unassigned"
                    shifts = schedule.get(current_day, {"AM": "Unassigned", "PM": "Unassigned"})
                    html_schedule += f"""
                    <td>
                        {current_day}<br>
                        <b>AM:</b> {shifts.get('AM', 'Unassigned')}<br>
                        <b>PM:</b> {shifts.get('PM', 'Unassigned')}
                    </td>
                    """
                    current_day += 1
            html_schedule += "</tr>"

        # Close the table and the HTML structure
        html_schedule += """
            </table>
        </body>
        </html>
        """

        # Write the HTML content to a file
        file_name = f"care_schedule_{year}_{month}.html"
        try:
            with open(file_name, "w") as file:
                file.write(html_schedule)
            print(f"Schedule successfully exported to {file_name}")
        except Exception as e:
            print(f"Error exporting schedule: {e}")
# Example of usage 
care_schedule = {
    1: {"AM": "Nurse Joy", "PM": "Dr. Oak"},
    5: {"AM": "Peter Parker", "PM": "Tony Stark"},
    12: {"AM": "Sherlock Holmes", "PM": "Dr. Watson"},
    30: {"AM": "Frodo Baggins", "PM": "Samwise Gamgee"},
}
# Exporting the data into an html file
ScheduleExporter.export_to_html(care_schedule, 2024, 12)
