To create a VBA macro that colors all header rows in yellow in the active sheet, follow these steps:

1. Open Microsoft Excel and press `Alt + F11` to open the VBA editor.
2. In the VBA editor, go to the `Insert` menu, then click on `Module`. This will create a new module.
3. Paste the following code in the newly created module:

```vba
Sub ColorHeaderRowsYellow()
    Dim ws As Worksheet
    Set ws = ActiveSheet

    With ws
        For i = 1 To .UsedRange.Rows.Count
            If .Cells(i, 1).EntireRow.FontStyle Like "**Bold*" Then
                .Rows(i).Interior.Color = RGB(255, 255, 194) 'Yellow color
            End If
        Next i
    End With
End Sub
```

4. Press `Ctrl + S` to save the module as a new macro-enabled workbook (`.xlsm`) or add it to an existing one by choosing `File > Save As`.
5. Close the VBA editor and go back to your Excel workbook.
6. To run the macro, press `Alt + F8`, select `ColorHeaderRowsYellow` from the list, and click `Run`. The header rows will now be colored in yellow.
7. If you want the macro to run automatically when the workbook is opened, go to the `ThisWorkbook` module by selecting it from the drop-down list at the top of the VBA editor, then paste the following code:

```vba
Private Sub Workbook_Open()
    ColorHeaderRowsYellow
End Sub
```

Now, when you open the workbook, all header rows will be colored in yellow.