---
title: Subprocesses in python
---
# `subprocess`

---

The `subprocess` module allows for execution of arbitrary external executables from the system.

One can think of it like a terminal.

# Basics

---

Subprocesses run inherently asynchronous.
Subprocesses run on the system directly, not in a shell (unless specified).
The programs available to run depend on the underlying system, the invocation doesn't, the library takes care of converting the parameters into a windows compatible `CreateProcess()` string.

# Constants

## File descriptors

- `DEVNULL`  
    The systems trashcan.
- `PIPE`  
    A connection for 2 processes.
- `STDOUT`  
    The standard output pipe or the current process.

## Exceptions

- `SubprocessError`
    The base error for this module.
- `TimeoutError`  
    Some timeout expired.
- `CalledProcessError`  
    The subprocess exited in an unexpected way.

# `Popen` class

---

The base class in this module is the `Popen` class.

The function signature may be confusing at first.

    Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None,
        stderr=None, preexec_fn=None, close_fds=True, shell=False,
        cwd=None, env=None, universal_newlines=False, startupinfo=None,
        creationflags=0, restore_signals=True, start_new_session=False,
        pass_fds=())


## Some important arguments

- `args`  
    The invocation arguments. Should be `tuple` or `list` of `strings` containing process name and arguments. Basically split the shell command on the spaces: `ls -A *.md ==> ['ls', '-A', '*.md']`.

---

- `shell` (default: `False`)  
    Executes in a shell. Should always be `False`, otherwise the call is unsafe.

- `stdout`, `stdin`, `stderr`  
    In- and output connections for the child process.  
    The `DEVNULL`, `PIPE` and `STDOUT` constants are often useful here.

---

- `env`  
    Environment variables for the child process. Default will be a subset of `os.environ` (python process environment).

- `cwd`  
    The working directory for the child process.

# Popen objects

---

When Popen is instantiated the underlying process starts executing, and the returned `Popen` object contains information about the running process.

---

## Getting information

- `process.args`  
    Get the arguments the process was called with.

- `obj.stdout`, `obj.stdin`, `obj.stderr`  
    In- and output connections as they were set during process initialization.

---

- `process.pid`  
    Process ID used by the system.

- `process.poll()`  
    Check if the process has terminated. Returns the returncode of the process. If it hasn't exited returns `None`.

- `process.returncode`  
    Attribute returned by function above. But does not check. Thus the above function should be used instead.

---

## Interacting with the process

- `process.wait(timeout=None)`  
    Wait for the process to terminate for *timeout* seconds. If *timeout* is `None` wait unit terminate indefinitely.

- `process.send_signal(signal)`  
    Send a signal to the process.

---

- `process.communicate(input=None, timeout=None)`  
    Write *input* data to the process's `stdin` (if `stdin` was `PIPE`), wait for process termination, read the processes `stdout` data (if `stdout` was `PIPE`) and return it. Timeout works as above.

---

- `process.terminate()`  
    Sends a termination signal to the process (`SIGTERM`).

- `process.kill()`  
    Force the process to terminate (`SIGKILL`).



## Popen with context manager

```python
with subprocess.Popen(['ls']) as process:
    pass
```

Closes file descriptors on exit and waits for the process.


# Convenience functions

---

The module provides shorthands for commonly used ways of using `Popen`. Note that all these internally just call `Popen`.

---

- `call`  

        call(args, *, stdin=None, stdout=None,
        stderr=None, shell=False, timeout=None)

    Calls a process, waits for termination and returns the returncode.

- `check_call(arguments as above)`  
    Calls a process, waits for termination, returns nothing if successful (returncode == 0), if unsuccessful raises a `CalledProcessError`.

---

- `check_output`  

        check_output(args, *, stdin=None, stdout=None,
        stderr=None, shell=False, timeout=None)

    Run the command and returns the output of the process. Also raises `CalledProcessError` if the returncode was not 0.
