# 
# Various logical constructions
# 

def precondition(value_of_precondition):
	if (value_of_precondition != True):
		raise PreconditionException

def postcondition(value_of_postcondition):
	if (value_of_postcondition != True):
		raise PostconditionException

def assertion(value_of_assertion):
	if (value_of_assertion != True):
		raise AssertionException

def progress(progress_value):
	# NOTE that we can't expect progess to be non-negative,
	# because some things like "fib" can skip "levels" and
	# ask for values for which the progress exp. is negative
	if not is_integer(progress_value) or False:

		# *** still need to check actual progress ***

		raise ProgessException

def loop_precondition(value_of_loop_precondition):
	if value_of_loop_precondition != True:
		raise LoopPreconditionException

def loop_postcondition(value_of_loop_postcondition):
	if value_of_loop_postcondition != True:
		raise LoopPostconditionException

def loop_invariant(value_of_loop_invariant):
	if value_of_loop_invariant != True:
		raise LoopInvariantException

def loop_progress(loop_progress_value):
	# NOTE that we can't expect progess to be non-negative,
	# because some things like "fib" can skip "levels" and
	# ask for values for which the progress exp. is negative
	if not is_integer(loop_progress_value) or False:

		# *** still need to check actual progress ***

		raise LoopProgressException

#
# And now, some things that will hopefully make "isinstance" less confusing...
#

def is_integer(v):
	return isinstance(v, int) or isinstance(v, long)

def is_number(v):
	return is_integer(v) or isinstance(v, float)

def is_string(v):
	return isinstance(v, basestring)

