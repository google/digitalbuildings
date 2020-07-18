package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IInlet_guidevane_percentage_sensor;
/**
* Class Igm 
* Inlet guidevane monitoring.
*/
public interface IIgm extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesInlet_guidevane_percentage_sensor (IInlet_guidevane_percentage_sensor parameter);

	public Set<IInlet_guidevane_percentage_sensor> getUsesInlet_guidevane_percentage_sensor();

}