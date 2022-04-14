from domain.parser import PDDLParser
from generator import MisereGenerator
from z3 import simplify
import time
import os

if __name__ == '__main__':
    start = time.time()
    # 1.Sub
    # 1.1 Take-away

    # pwd = "pddl/1.Sub/1.1 Take-away/Take-away-8.pddl"

    # domain = PDDLParser('pddl/1.Sub/1.1 Take-away/Take-away-2.pddl')    #Y
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-3.pddl")    #Y
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-4.pddl")    #Y
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-5.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-6.pddl")  #Y
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-7.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-8.pddl")  #Y

    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-9.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-10.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-11.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-12.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-13.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-14.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-15.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-16.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-17.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-18.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-19.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-20.pddl") #N
    # # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-21.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-22.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-23.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-24.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-25.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-26.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-27.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-28.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-29.pddl") #N
    # domain = PDDLParser("pddl/1.Sub/1.1 Take-away/Take-away-30.pddl") #N
    # 1.2 Subtraction
    # pwd = "pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,5).pddl"
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1).pddl") #Y,策略没有出来
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,5).pddl")  # N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,3,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,2,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,3,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(1,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2).pddl")  #Y
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,3,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,9,10).pddl")  #N

    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(2,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(3,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(4,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(5,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(6,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(7,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(8).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(8,9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(8,9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(8,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(9).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(9,10).pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.2 Subtraction/Subtraction-(10).pddl")  #N

    # 1.3 S,D-MarkGame
    # pwd = "pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{2,4}.pddl"
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/t,d-i-Mark-Game{2,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{2,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{2,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{2,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{3,9}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,7}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{4,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,7}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{5,9}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{6,9}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,7}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{7,9}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,7}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{8,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,2}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,3}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,4}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,5}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,6}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,7}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,8}.pddl")  #N
    # domain = PDDLParser("pddl/1.Sub/1.3 S, D-MarkGame/T,d-I-Mark-Game{9,9}.pddl")  #N

    # 2. Nim
    # 2.1 Nim
    # pwd = "pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-2).pddl"
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-1).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-2).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-3).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-4).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim(v3-le-5).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Three-piled-nim.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.1 Nim/Two-piled-nim.pddl")  #Y
    # 2.2 Monotonic Nim
    # pwd = "pddl/2.Nim/2.2 Monotonic Nim/Monotonic-3-piled-Nim.pddl"
    # domain = PDDLParser("pddl/2.Nim/2.2 Monotonic Nim/Monotonic-2-piled-Nim.pddl")  #Y
    # domain = PDDLParser("pddl/2.Nim/2.2 Monotonic Nim/Monotonic-3-piled-Nim.pddl")  #Y
    # 2.3 Empty and Transfer
    # pwd = "pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le2.pddl"
    # domain = PDDLParser("pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le1.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le2.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le3.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le4.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.3 Empty and Transfer/Empty-and-Transfer(n=3)v3le5.pddl")  #N
    # 2.4 Empty All But One
    # pwd = "pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le1.pddl"
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3).pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le1.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le2.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le3.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le4.pddl")  #N
    # domain = PDDLParser("pddl/2.Nim/2.4 Empty All But One/Empty-All-But-One(n=3)v3le5.pddl")  #N
    # 2.5 Empty and Redistribute(跑不了)
    # pwd = "pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le1.pddl"
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3).pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le1.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le2.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le3.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le4.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.5 Empty and Redistribute/Empty-and-Redistribute(n=3)v3le5.pddl")  #
    # 2.6 Entropy Reduction Game(跑不了)
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=2).pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3).pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3)v3le1.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3)v3le2.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3)v3le3.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3)v3le4.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.6 Entropy Reduction Game/Entropy-Reduction-Game(n=3)v3le5.pddl")  #
    # 2.7 Min Game(跑不了)
    # pwd = "pddl/2.Nim/2.7 Min Game/Min-Gamev2le2.pddl"
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Game.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Gamev2le1.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Gamev2le2.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Gamev2le3.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Gamev2le4.pddl")  #
    # domain = PDDLParser("pddl/2.Nim/2.7 Min Game/Min-Gamev2le5.pddl")  #

    gen = MisereGenerator(domain,pwd)
    formula_template = gen.generate_formula(0,0)
    formula = simplify(formula_template.formula_model())
    cost1 = time.time() - start
    print('*' * 50)
    print('N-formula:\n\t %s' % formula)

    strategies = gen.generate_strategy()
    cost2 = time.time() - start
    print('*' * 50)
    print('strategies:\n', strategies)

    if not os.path.exists("./log"):
        os.mkdir("./log")
    with open("./log/%s" % domain.name, "a") as f:
        print("\n*******************Finished*******************")
        print('N-formula:\n\t %s' % formula)
        print('time cost:\n\t %s' % cost1)
        print('strategies:\n\t %s' % strategies)
        print('time cost:\n\t %s' % cost2)

        print('\nmisere rule', file=f)
        print('N-formula:\t %s' % formula, file=f)
        print('time cost:\t %s' % cost1, file=f)
        print('strategies:\t %s' % strategies, file=f)
        print('time cost:\t %s' % cost2, file=f)
