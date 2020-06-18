	.file	"map.cpp"
	.text
	.section	.rodata
	.align 8
.LC0:
	.string	"- FIGURE?, UMKC,XYZHello Folks,TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs UJq TNn*RPn/QPbEWS_JSWQAIJO^NBELPeHBFHT}TnALVlBLOFAkHFOuFETpHCStHAUFAgcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm SOn TNn ULo0ULo#ULo-WHq!WFs XDt!"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$10, -4(%rbp)
	movl	-4(%rbp), %eax
	movl	%eax, -8(%rbp)
.L7:
	movl	-8(%rbp), %eax
	leal	1(%rax), %edx
	movl	%edx, -8(%rbp)
	addl	$21, %eax
	movslq	%eax, %rdx
	leaq	.LC0(%rip), %rax
	movzbl	(%rdx,%rax), %eax
	movsbl	%al, %eax
	movl	%eax, -12(%rbp)
	cmpl	$0, -12(%rbp)
	setne	%al
	testb	%al, %al
	je	.L2
.L6:
	movl	-12(%rbp), %eax
	leal	-1(%rax), %edx
	movl	%edx, -12(%rbp)
	cmpl	$64, %eax
	setg	%al
	testb	%al, %al
	je	.L7
	addl	$1, -4(%rbp)
	cmpl	$90, -4(%rbp)
	jne	.L4
	movl	-4(%rbp), %ecx
	movl	$954437177, %edx
	movl	%ecx, %eax
	imull	%edx
	sarl	%edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	jmp	.L5
.L4:
	movl	-8(%rbp), %eax
	andl	$1, %eax
	xorl	$33, %eax
.L5:
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L6
.L2:
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
