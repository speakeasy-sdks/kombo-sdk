# PostHrisEmployeesSuccessfulResponseEmploymentStatus

The current employment status of the employee:

- `ACTIVE`: the employee is **actively employed**
- `PENDING`: the employee is **not actively employed yet** (but they signed their contract or are part of an onboarding process)
- `INACTIVE`: the employee is **not actively employed** anymore
- `LEAVE`: the employee is still employed but **currently on leave** (note that not all HR systems support this status — use our absences API for detailed information)

Please note that in rare cases, where we can't find a clear mapping, the original string is passed through.


## Supported Types

### PostHrisEmployeesSuccessfulResponse1

```python
postHrisEmployeesSuccessfulResponseEmploymentStatus: shared.PostHrisEmployeesSuccessfulResponse1 = /* values here */
```

### 

```python
postHrisEmployeesSuccessfulResponseEmploymentStatus: str = /* values here */
```

