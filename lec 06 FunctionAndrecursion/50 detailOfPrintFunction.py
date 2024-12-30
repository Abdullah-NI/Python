# (function) def print(
#     *values: object,                       # jo value pass kari
#     sep: str | None = " ",                  # jab , lagakar likhte hai tpo ye sep apne aap space de deta hai
#     end: str | None = "\n",                 #jab line end hoti hai to ye \n de deta hai
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None
print("abdullah","Affan")  #sep=" "  yaha sep ne space diya yadi me sep ko kuch aur lijh likh do to space ki gaha wo ayga
print("abdullah","affan",sep="  TAb  ")

print()

print("Abdullah")   #end="\n"  yaha end ne next line di if ise hatani hai end me wo pass kar do jo tum chate ho
print("Affan")

print("Abdullah",end=" ")  #ab line puri hone per space ayga
print("Affan")