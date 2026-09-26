# Sample / solution

## Why this approach works
Naming the shape works because the model will always produce something, and if you do not choose the container it chooses prose. Operations runs on rows and fields: a table with named columns can be sorted, filtered, and imported into a ticket system, while a well-written paragraph about the same three complaints cannot. Naming the columns matters as much as naming the container, because unnamed columns become invented columns, and an invented column is a silent failure that only surfaces downstream. The weaker instinct is a long paragraph of instructions that describes the data instead of constraining the output; the failure mode is a lovely summary someone re-types into a spreadsheet by hand, which is exactly where transcription errors enter an official record.

## A complete solution
The chat post, exactly as sent to the model: `Normalize this for operations review. Return a table with columns: issue, location, date, priority, next action.`

Against M1 ("Three complaints: missed pickup, broken sign, water leak. Locations: Bank St, Elgin St, Bronson Ave. Dates: Jan 3, Jan 4, Jan 5."), that instruction returns:

- missed pickup | Bank St | Jan 3 | medium | schedule make-up collection
- broken sign | Elgin St | Jan 4 | low | dispatch sign crew
- water leak | Bronson Ave | Jan 5 | high | dispatch utility crew today

The tricky part is the priority column, and it is worth narrating in class. M1 never states priorities, so a student might object that asking for priority invites invention. The defense: the column is named precisely so the judgment stays visible. A water leak outranking a broken sign is the call an operations supervisor would make, and putting it in a named column means a human reviews the inference instead of the model hiding it inside prose. The same logic covers the dates: naming "date" as a column forces the model to keep Jan 3 aligned with Bank St row by row, which is the alignment that quietly collapses in a flowing summary. If your consumer is a ticket system rather than a person, the same five fields become a JSON request, `Return JSON with keys: issue, location, date, priority, next_action`, and the lesson holds either way: you state the schema, or the model does.
