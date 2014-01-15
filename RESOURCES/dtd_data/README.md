## DTD exercises

 1. Validation. Use
 
        xmllint --valid --noout <filename>

 1. `<!DOCTYPE countries [ ... ]>` for frame holding `<!ELEMENT ...>` items
 1. `<!ELEMENT <element name> (<child names>)>`: for all elements at any level of depty
 1. `<!ATTLIST <element name> <attribute name> <type> <required or implied>>` for attributes of an element, placed under the element in question (?)
 1. `<!ELEMENT name (#PCDATA)>`: for text-content
 1. `<!ELEMENT Courseref EMPTY>`: for self-closing tags
 1. `<!ELEMENT Department (Title,(Course|Professor|Lecturer)*)>`: to combine required with Kleene-starred items
 1. `<!ELEMENT Description (#PCDATA|Courseref)*>`: for cases where an element may either contain text or a child element (the child element appearing within the text)
 1. `<!ATTLIST language percentage CDATA #REQUIRED>`: for attributes with required content
 1. `<!ATTLIST country population CDATA #IMPLIED>`: for attributes with optional content

----

 1. **Questions**: What id the difference between `ID`, `IDREF`, and `IDREFS`?
   1. `<!ATTLIST Course Number ID #REQUIRED>`: Here a `Course` is assigned a `Number` that will be referred to elsewhere in the DTD as 

        <!ELEMENT Courseref EMPTY>
            <!ATTLIST Courseref 
                Number IDREF #REQUIRED>`

      and in the XML as
      
        <Course Number="CS221" Prerequisites="CS107" Instructors="AN ST" Enrollment="180">
            ... 
        </Course>

   1. `<!ATTLIST Course Instructors IDREFS #REQUIRED>`: Here `Instructors` is assigned a **list** of IDs — the IDs themselves are initialized under `Professor` or `Lecturer`.
   1. `<!ATTLIST Department Chair IDREF #REQUIRED>`: Here `Chair` is assigned a unique ID (hence not `IDREFS` but `IDREF` — the IDs themselves are initialized under `Professor` or `Lecturer` in the DTD as
   
        <!ELEMENT Professor (First_Name,Middle_Initial?,Last_Name)> <!ATTLIST Professor InstrID ID #REQUIRED>

      and in the XML as 

            <Professor InstrID="AA">
              <First_Name>Alex</First_Name>
              <Middle_Initial>S.</Middle_Initial>
              <Last_Name>Aiken</Last_Name>
            </Professor> 

      in the XML proper.

[end]