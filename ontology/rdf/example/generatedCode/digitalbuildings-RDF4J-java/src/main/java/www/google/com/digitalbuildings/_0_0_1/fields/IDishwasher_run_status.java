package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IDishwasher;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;

public interface IDishwasher_run_status extends IField{

	public IRI iri();

    public void addComposedOfDishwasher (IDishwasher parameter);

	public Set<IDishwasher> getComposedOfDishwasher();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}