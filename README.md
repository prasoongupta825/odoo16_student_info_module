# odoo16_student_info_module
Interview Task - Students Marks Info


Assign Roll Number Button

To implement the Student Roll Number sequence with the provided details, follow these steps:

In the Odoo backend, go to Settings.
Under the Technical section, select Sequences & Identifiers.
Click on Create to create a new sequence.
In the Sequence Code field, enter 'student.roll.number'.
In the Name field, enter 'Student Roll Number Sequence'.
Set the Active field to True to activate the sequence.
Set the Prefix field as per your requirement (e.g., 'XX-YY-').
Leave the Suffix field empty if you don't need a suffix.
Ensure that the Use subsequences per date_range field is unchecked.
Set the Sequence Size field to 0 if you don't want to limit the sequence size.
Set the Step field to 1.
Set the Next Number field to 0 initially.
Click on Save to create the sequence.
Once you have created the sequence, you can use it in your code to generate roll numbers for students.

Note: Adjust the prefix ('XX-YY-') according to your desired format.
