module.exports = {
  apps : [{
    name        : "backend_school_task",
    script      : "./run.py",
    watch       : true,
    interpreter : "./env/bin/python3",
    ignore_watch: ["./data"]
  }]
}
