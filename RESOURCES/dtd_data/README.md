## DTD exercises

  1. Validation. At the command line use
 
        xmllint --valid --noout <filename>

  1. Types of entry:

   * Use `<!DOCTYPE countries [ ... ]>` for frame holding `<!ELEMENT ...>` items
   * Use `<!ELEMENT <element name> (<child names>)>`: for all elements at any level of depty
   * Use `<!ATTLIST <element name> <attribute name> <type> <required or implied>>` for attributes of an element, placed under the element in question (?)

  1. Issues surrounding `ELEMENT`:

   * Use `<!ELEMENT <element name> (#PCDATA)>`: for text-content
   * Use `<!ELEMENT <element name> EMPTY>`: for self-closing tags
   * Use `<!ELEMENT <element name> (Title,(Course|Professor|Lecturer)*)>`: to combine required with Kleene-starred items
   * Use `<!ELEMENT <element name> (#PCDATA|Courseref)*>`: for cases where an element may either contain text or a child element (the child element appearing within the text)

  1. Issues surrounding `ATTLIST`:

    * Use `<!ATTLIST <element name> <attribute name> CDATA #REQUIRED>`: for attributes with required content
    * Use `<!ATTLIST <element name> <attribute name> CDATA #IMPLIED>`: for attributes with optional content

----

**Questions**

 1. If the type of an attribute is not `CDATA`, what kinds of pointers can be used? Answer: `ID`, `IDREF`, and `IDREFS`.
 1. What id the difference between `ID`, `IDREF`, and `IDREFS`?

   * **ID**: `<!ATTLIST Course Number ID #REQUIRED>`: Here a `Course` is assigned a `Number` that will be referred to elsewhere in the DTD as 

        <!ELEMENT Courseref EMPTY>
            <!ATTLIST Courseref 
                Number IDREF #REQUIRED>`

      and in the XML as
      
        <Course Number="CS221" Prerequisites="CS107" Instructors="AN ST" Enrollment="180">
            ... 
        </Course>

   * **IDREF**: `<!ATTLIST Department Chair IDREF #REQUIRED>`: Here `Chair` is assigned a unique ID (hence not `IDREFS` but `IDREF` — the IDs themselves are initialized under `Professor` or `Lecturer` in the DTD as
   
        <!ELEMENT Professor (First_Name,Middle_Initial?,Last_Name)> <!ATTLIST Professor InstrID ID #REQUIRED>

      and in the XML as 

            <Professor InstrID="AA">
              <First_Name>Alex</First_Name>
              <Middle_Initial>S.</Middle_Initial>
              <Last_Name>Aiken</Last_Name>
            </Professor>

   * **IDREFS**: `<!ATTLIST Course Instructors IDREFS #REQUIRED>`: Here `Instructors` is assigned a **list** of IDs — the IDs themselves are initialized under `Professor` or `Lecturer`.

[end]