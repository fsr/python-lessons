# mit `str.format()`  

'my string {} {}'.format(4, 'vier')
# in Reihenfolge der argumente

'my string {number} {name}'.format(name='vier', number=4)`
# via Name, Reihenfolge egal

'my string {number} {}'.format('vier', number=4)
# oder beides kombiniert

# und mit dem %-Operator

'string %d %s' % (4, 'vier')
# in Reihenfolge

'string %(number)d %(name)s' % {number:4, name:'vier'}
# via Name
