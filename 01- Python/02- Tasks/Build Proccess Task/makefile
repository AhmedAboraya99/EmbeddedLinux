#prepared by : Ahmed Aboraya
# Define the toolchain and flags
CC = arm-none-eabi-gcc
LD = arm-none-eabi-gcc
OBJCOPY = arm-none-eabi-objcopy
CFLAGS = -mcpu=cortex-m4 -mthumb -mfloat-abi=soft -mfpu=fpv4-sp-d16 -std=c11 -Wall -gdwarf-2 -g
LDFLAGS = -mcpu=cortex-m4 -T STM32F401CCUX_FLASH.ld --specs=nosys.specs -Wl,-Map="STM_ARM_RTO.map" -Wl,--gc-sections -static --specs=nano.specs -mthumb -mfloat-abi=soft -mfpu=fpv4-sp-d16 -Wl,--start-group -lc -lm -Wl,--end-group

# Define the source files and object files
SRCS = $(wildcard *.c) startup_stm32f401ccux.s
OBJS = $(SRCS:.c=.o) $(SRCS:.s=.o)

#prepared by : Ahmed Aboraya
# Define the toolchain and flags
CC = arm-none-eabi-gcc
LD = arm-none-eabi-ld
OBJCOPY = arm-none-eabi-objcopy

# Define the source files and object files
SRCS = $(wildcard *.c)
AS =  $(wildcard *.s) #all assembly files
OBJS = $(SRCS:.c=.o) $(AS:.s=.o)

# Define the output file
OUTFILE = STM_ARM_RTO


# Define the build rule
all: $(OUTFILE).bin


# Define the ELF file rule
$(OUTFILE).elf: $(OBJS)
	$(CC) $(OBJS) $(LDFLAGS) -o $@

# Define the hex file rule
$(OUTFILE).hex: $(OUTFILE).elf
	$(OBJCOPY) -O ihex $< $@
# Define the bin file rule
$(OUTFILE).bin: $(OUTFILE).elf
	$(OBJCOPY) -O binary $< $@

# Define the object file rules
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.s
	$(CC) $(CFLAGS) -c $< -o $@


clean_all:
	rm -rf *.o *~ *.elf *.hex *.bin
	@echo "Everything is clean"
	
clean:
	rm *.elf *.hex *.bin
	@echo "Remove Build files"