# Sample / solution

## Why this approach works
The model will always produce something, and if you do not choose the container it chooses prose, which no ticket system can import. Naming the columns matters as much as naming the container, because unnamed columns become invented columns, a silent failure that only surfaces downstream.

## A complete solution
The chat post, exactly as sent to the model: `Normalize this for operations review. Return a table with columns: issue, location, date, priority, next action.`

Against M1 ("Three complaints: missed pickup, broken sign, water leak. Locations: Bank St, Elgin St, Bronson Ave. Dates: Jan 3, Jan 4, Jan 5."), that instruction returns:

- missed pickup | Bank St | Jan 3 | medium | schedule make-up collection
- broken sign | Elgin St | Jan 4 | low | dispatch sign crew
- water leak | Bronson Ave | Jan 5 | high | dispatch utility crew today

The tricky part is priority: M1 never states one. The column is named precisely so the judgment stays visible; a water leak outranking a broken sign is the call an operations supervisor would make, and a named column means a human reviews the inference instead of the model hiding it inside prose. If your consumer is a ticket system rather than a person, the same five fields become a JSON request, `Return JSON with keys: issue, location, date, priority, next_action`; either way, you state the schema or the model does.
