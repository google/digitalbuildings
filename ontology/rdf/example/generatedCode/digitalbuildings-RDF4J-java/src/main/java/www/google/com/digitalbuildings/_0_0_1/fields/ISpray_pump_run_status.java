package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpray;
import www.google.com.digitalbuildings._0_0_1.subfields.IPump;

public interface ISpray_pump_run_status extends IField{

	public IRI iri();

    public void addComposedOfPump (IPump parameter);

	public Set<IPump> getComposedOfPump();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

    public void addComposedOfSpray (ISpray parameter);

	public Set<ISpray> getComposedOfSpray();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}