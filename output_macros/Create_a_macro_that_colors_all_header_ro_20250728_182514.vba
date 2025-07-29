To create a VBA macro that colors the header rows of the active sheet yellow, follow these steps:

1. Press `Alt + F11` to open the VBA Editor.
2. In the Project Explorer (left side), make sure you are in the correct project (usually [Project1] or the name of your workbook).
3. Right-click on "Module" under the VBAProject (Objects) and select "Insert Module".
4. Copy and paste the following code into the newly inserted module:

```vba
Sub ColorHeaderRowsYellow()
    Dim ws As Worksheet
    Dim rng As Range

    Set ws = ActiveSheet

    With ws
        Set rng = .UsedRange.Rows(1)

        While rng.CountLarge > 0 And rng.Cells(rng.CountLarge, .Columns.Count).Column <= .Columns.Count
            If rng.Interior.ColorIndex = xlNone Then
                rng.Interior.Color = RGB(255, 255, 160) ' Yellow color (RGB(255, 255, 160))
            End If
            Set rng = rng.Rows(1).Resize(rng.Rows.Count - 1)
        Wend
    End With
End Sub
```

5. Press `Ctrl + S` to save the module and give it a name, for example "ColorHeaderYellow".
6. Close the VBA Editor.
7. Press `Alt = F8`, select "ColorHeaderYellow" and click on Run. This will run the macro and color the header rows in yellow.

Alternatively, you can assign the macro to a button or shortcut key for easier access. To do this:

1. Insert a command button on your worksheet (Developer tab > Insert > Button).
2. Right-click on the new command button and select "Assign Macro".
3. Select the "ColorHeaderYellow" macro from the list and click OK. The command button will now run the macro when clicked.