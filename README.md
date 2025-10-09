# capstone-project
Capstone project for course



Testing:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | Value    |
| Row 2    | More     | Info     |
| Row 3    | Example  | Entry    |


- navigation controls appear when pagination threshold is reached for main page / index.html - pass
- navigation controls appear when pagination threshold is reached for my_systems.html - pass

    Testing exceptions:

    - where the error: 
    # type: ignore was used to suppress these false reports of errors. Good hygiene with regards to incorrect error messages is important in becuase it maintains focus on real error messages



Bugs and issues:

- cloudinary not auto delete
- when editing system details, the name of the existing featured_image that was originally uploaded to cloudinary is not shown

it is possible to input negative prices into the number field for prices. This is not within the intended parameters of the page, but as the numbers are not used in any type of calculation or for filtering, any issue is localised to the particular records.

Edit: actually, being able to use a negative price values to support the idea that a system would be so bad they'd have to pay you to take it is, in-fact, in keeping with the spirit of the site. This is by happenstance though, and not by design.


Features:

- A user cannot review their own system
- A user can only review a system once