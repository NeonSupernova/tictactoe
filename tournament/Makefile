# Define variables
BOTS_DIR = bots
DRIVERS_DIR = drivers

# Executables to build/copy
C_DRIVER = $(BOTS_DIR)/bot_c/bot
CPP_DRIVER = $(BOTS_DIR)/bot_cpp/bot
JAVA_DRIVER = $(BOTS_DIR)/bot_java/bot
RUST_DRIVER = $(BOTS_DIR)/bot_rs/bot

# Scripts (just copy these)
PY_DRIVER = $(BOTS_DIR)/bot_py/bot
JS_DRIVER = $(BOTS_DIR)/bot_js/bot
LISP_DRIVER = $(BOTS_DIR)/bot_lisp/bot
LUA_DRIVER = $(BOTS_DIR)/bot_lua/bot
SH_DRIVER = $(BOTS_DIR)/bot_sh/bot

# Directories for bots
BOT_DIRS = $(addprefix $(BOTS_DIR)/, bot_c bot_cpp bot_java bot_rs bot_py bot_js bot_lisp bot_lua bot_sh)

# Create the bot directories and copy config.toml
all: $(BOT_DIRS) $(C_DRIVER) $(CPP_DRIVER) $(JAVA_DRIVER) $(RUST_DRIVER) \
     $(PY_DRIVER) $(JS_DRIVER) $(LISP_DRIVER) $(LUA_DRIVER) $(SH_DRIVER)

# Create bot directories
$(BOT_DIRS):
	mkdir -p $@

# Generate config.toml with the correct run command
$(BOTS_DIR)/bot_c/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "./bot"' > $@

$(BOTS_DIR)/bot_cpp/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "./bot"' > $@

$(BOTS_DIR)/bot_java/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "java bot_java.TicTacToeAI"' > $@

$(BOTS_DIR)/bot_rs/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "./bot"' > $@

$(BOTS_DIR)/bot_py/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "python3 bot"' > $@

$(BOTS_DIR)/bot_js/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "node bot"' > $@

$(BOTS_DIR)/bot_lisp/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "clisp bot"' > $@

$(BOTS_DIR)/bot_lua/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "lua bot"' > $@

$(BOTS_DIR)/bot_sh/config.toml:
	echo '[author]\nname = "Your Name Here"\nnotes = ""\n\n[bot]\nrun = "bash bot"' > $@

# Compile C driver and create config.toml
$(C_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.c $(BOTS_DIR)/bot_c/config.toml
	clang -o $@ $<

# Compile C++ driver and create config.toml
$(CPP_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.cpp $(BOTS_DIR)/bot_cpp/config.toml
	clang++ -o $@ $<

# Compile Java driver and create config.toml
$(JAVA_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.java $(BOTS_DIR)/bot_java/config.toml
	javac -d $(BOTS_DIR)/bot_java $<
	mv $(BOTS_DIR)/bot_java/TicTacToeAI.class $@

# Compile Rust driver and create config.toml
$(RUST_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.rs $(BOTS_DIR)/bot_rs/config.toml
	rustc -o $@ $<

# Copy Python script and create config.toml
$(PY_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.py $(BOTS_DIR)/bot_py/config.toml
	cp $< $@

# Copy JavaScript script and create config.toml
$(JS_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.js $(BOTS_DIR)/bot_js/config.toml
	cp $< $@

# Copy Lisp script and create config.toml
$(LISP_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.lisp $(BOTS_DIR)/bot_lisp/config.toml
	cp $< $@

# Copy Lua script and create config.toml
$(LUA_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.lua $(BOTS_DIR)/bot_lua/config.toml
	cp $< $@

# Copy Bash script and create config.toml
$(SH_DRIVER): $(DRIVERS_DIR)/TicTacToeAI.sh $(BOTS_DIR)/bot_sh/config.toml
	cp $< $@

# Clean all compiled files and directories
clean:
	rm -rf $(BOTS_DIR)/bot_*

.PHONY: all clean