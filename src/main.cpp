#include <vector>
#include <array>
#include <cstdint>
#include <regex>
#include <string>
#include <string_view>
#include <iostream>
#include <any>
#include <algorithm>


template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T> vec)
{
    char quote = 0;
    os << '[';
    for(auto i = vec.begin(), end = vec.end(), last = vec.end() - 1; i != end; ++i){
        if constexpr (
            std::is_same<T, std::string>::value      || 
            std::is_same<T, std::string_view>::value ||
            std::is_same<T, const char *>::value     ||
            std::is_same<T, char *>::value)
        {
            if constexpr (std::is_same<T, std::string>::value || 
            std::is_same<T, std::string_view>::value) {
                if(i->size() == 1){
                    quote = '\'';

                } else {
                    quote = '"';
                }
            } else {
                quote = '"';
            }

            os << quote << *i << quote;
        } else {
            os << *i;
        }
        if(i != last){
            os << ',';
        }
    }
    os << ']';
    return os;
}

typedef std::basic_string<std::any> node_t;

template<typename T>
auto par(std::vector<T> tokens){
    node_t stack;
    std::uint_fast8_t j = 1;
    for(const auto& current_token : tokens){
        if(current_token == ")"){
            
        }
    }
    return 0;
}

double calc(const std::string& eq){
    const static std::regex rgx(R"([*\/]{2}|[()*\/+-.^]|\d+)");
    std::sregex_token_iterator i{
        eq.begin(), eq.end(),
        rgx,
    }, end;
    std::vector<std::string> tokens{i, end};
    std::cout << eq << " -> "<< tokens << std::endl;
    auto groups = par(tokens);
    return 0;
}

int main(int argc, char **argv_c){
    const std::vector<std::string> argv{argv_c, argv_c + argc};
    if(argc <= 1){
        std::cout << "ExpressionSolver <equation>\n";
        exit(1);
    }
    calc(argv[1]);
    return 0;
}
