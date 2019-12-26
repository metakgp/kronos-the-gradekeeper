using JSON

if (length(ARGS) != 3)
    error("Arguments must have `filepath`, `year` and `sem`") 
end
filepath = ARGS[1]
year = ARGS[2]
sem = ARGS[3]

stripp(x) = strip.(x)
custom_split_delim(x) = split(x, ',')
lines = readlines(filepath)
formatted_lines = stripp.(custom_split_delim.(replace.(lines, "\"" => "")))

mutable struct Course
    code::String
    name::String
    EX::Int
    A::Int
    B::Int
    C::Int
    D::Int
    P::Int
    F::Int
    X::Int
    Y::Int
    N::Int
end

Course(code, name) = Course(code, name, zeros(Int, 10, 1)...)

grades = ["A", "B", "C", "D", "P", "F", "X", "N", "Y", "EX"]

function show_course(c::Course)
    println("CourseCode: $(c.code) ($(c.name)) has grades")
    for g in grades
        println(" $(g) has grade: ", getproperty(c, Meta.parse(eval(g))))
    end
end

function format_grades_yearly_format(c::Course)
    _dict = Dict{String, Any}()
    for g in grades
        _dict[g] = getproperty(c, Meta.parse(eval(g)))
    end
    return _dict
end

courses_found = Array{Course, 1}()
cache = Dict{String, Int}()

for j in eachindex(formatted_lines)
    line = formatted_lines[j]
    print(j)
    for i in eachindex(line)
        entry = strip(line[i])
        if match(r"^[A-Z]{2}[0-9]{5}$", entry) != nothing
            if get(cache, entry, -1) == -1
                cache[entry] = length(courses_found) + 1
                push!(courses_found, Course(entry, strip(line[i+1])))
            end
            if line[i+2] ∉ grades && line[i+2] != ""
#            if entry ∈ ("ME31007",  "CY41005", "IM21001", "ME39007")
                grade = Meta.parse(eval(strip(line[i+3])))
            else
                grade = Meta.parse(eval(strip(line[i+2])))
            end
            grade == nothing && continue
            setproperty!(courses_found[cache[entry]], grade, getproperty(courses_found[cache[entry]], grade) + 1)
        end
    end
    println("")
end

all_data = JSON.parsefile("yearWiseGrades.json")
year_sem = year * sem

for c in courses_found
    if get(all_data, c.code, -1) != -1 
        all_data[c.code][year_sem] = format_grades_yearly_format(c)
    else
        all_data[c.code] = Dict{String,Any}(year_sem => format_grades_yearly_format(c))
    end
end

open("yearWiseGrades.json", "w") do f
    JSON.print(f, all_data)
end

courses_info = JSON.parsefile("../courses.json")

for c in courses_found
    if get(courses_info, c.code, -1) == -1
        courses_info[c.code] = Dict{String, Any}("id" => c.code, "name" => c.name)
    end
end

open("../courses.json", "w") do f
    JSON.print(f, courses_info)
end

