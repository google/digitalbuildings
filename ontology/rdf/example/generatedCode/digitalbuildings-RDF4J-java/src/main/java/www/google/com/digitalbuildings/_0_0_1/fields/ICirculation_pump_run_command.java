package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.ICirculation;
import www.google.com.digitalbuildings._0_0_1.subfields.IPump;

public interface ICirculation_pump_run_command extends IField{

	public IRI iri();

    public void addComposedOfCirculation (ICirculation parameter);

	public Set<ICirculation> getComposedOfCirculation();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfPump (IPump parameter);

	public Set<IPump> getComposedOfPump();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

}