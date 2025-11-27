cmake_minimum_required(VERSION 3.16)
project(OBINexus_Policy VERSION 1.0.0 LANGUAGES C)

# OBINexus compatibility requirements
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Integration with existing OBINexus build orchestration
find_package(PkgConfig REQUIRED)
pkg_check_modules(OBINEXUS_CORE REQUIRED obinexus-core)
pkg_check_modules(DIRAM_RUNTIME REQUIRED diram-runtime)

# Policy framework library
add_library(polic STATIC
    src/core/polic_core.c
    src/core/resolution_engine.c
    src/data_structures/map_trie.c
    src/integration/nexus_search_bridge.c
)

target_include_directories(polic PUBLIC include)
target_link_libraries(polic ${OBINEXUS_CORE_LIBRARIES} ${DIRAM_RUNTIME_LIBRARIES})

# Client SDK library
add_library(polic_client_sdk STATIC
    src/client/policy_client_sdk.c
    src/client/qa_validation.c
)

target_link_libraries(polic_client_sdk polic)
